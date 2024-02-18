import time
import uuid
from functools import partial
from typing import Optional, List, Union, Dict

from pydantic import BaseModel
from pymilvus import Connections, Collection, FieldSchema, DataType, CollectionSchema, Hit
from pymilvus.client.abstract import MutationResult

from lemon_rag.lemon_runtime import models
from lemon_rag.llm.client.base_client import get_embedding_function
from lemon_rag.protocols.chat import CardComponentType, BusinessDataType, BusinessType
from lemon_rag.utils import log

default_index_schema = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}

embed_sentence = get_embedding_function("embed_knowledge_base_sentence")
embed_message_component = get_embedding_function("embed_message_component")
embed_candidate = get_embedding_function("embed_candidate")


class DocSearchRes(BaseModel):
    doc_id: int
    id: int


class CandidateSearchRes(BaseModel):
    vectorization_key: str
    business_id: int


class VectorAccess(BaseModel):
    connections: Optional[Connections] = None
    knowledge_base_collection: Optional[Collection] = None
    message_collection: Optional[Collection] = None
    candidate_collection: Optional[Collection] = None
    initialized: bool = False
    init_msg: str = ""

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init(self):
        if self.initialized:
            if self.init_msg:
                raise ValueError(f"milvus init failed for {self.init_msg}")
            return

        milvus_token: Optional[models.VectorStoreConfig] = models.VectorStoreConfig.get_or_none()
        if not milvus_token:
            self.initialized = True
            self.init_msg = "no milvus config found"
            raise ValueError("no milvus config found")
        connections = Connections()
        connections.connect("default", uri=milvus_token.uri, token=milvus_token.token)
        self.connections = connections
        self._init_collections()
        self.initialized = True

    def _init_collections(self):
        # self.knowledge_base_collection = self.prepare_collection(
        #     "document_rag",
        #     CollectionSchema([
        #         FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
        #         FieldSchema(name="raw_content", dtype=DataType.VARCHAR, max_length=2048),
        #         FieldSchema(name="doc_name", dtype=DataType.VARCHAR, max_length=256),
        #         FieldSchema(name="doc_id", dtype=DataType.INT32),
        #         FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=1536),
        #     ])
        # )
        self.message_collection = self.prepare_collection(
            "message_components",
            CollectionSchema([
                FieldSchema(name="id", dtype=DataType.VARCHAR, max_length=36, is_primary=True),
                FieldSchema(name="user_id", dtype=DataType.INT64),
                FieldSchema(name="session_id", dtype=DataType.INT64),
                FieldSchema(name="msg_pk", dtype=DataType.INT64),
                FieldSchema(name="msg_id", dtype=DataType.INT64),
                FieldSchema(name="component_type", dtype=DataType.VARCHAR, max_length=32),
                FieldSchema(name="vectorization_key", dtype=DataType.VARCHAR, max_length=2048),
                FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=1536),
            ])
        )
        self.candidate_collection = self.prepare_collection(
            "combobox_candidates",
            CollectionSchema([
                FieldSchema(name="id", dtype=DataType.VARCHAR, max_length=36, is_primary=True),
                FieldSchema(name="user_id", dtype=DataType.INT64),
                FieldSchema(name="business_id", dtype=DataType.INT64),
                FieldSchema(name="type", dtype=DataType.VARCHAR, max_length=32),
                FieldSchema(name="vectorization_key", dtype=DataType.VARCHAR, max_length=2048),
                FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=1536),
            ])
        )

    def prepare_collection(self, name: str, schema: CollectionSchema) -> Collection:
        c = Collection(name, schema=schema)
        if not c.has_index():
            c.create_index("vector", default_index_schema)
        c.load()
        return c

    def save_message(
            self,
            message: models.MessageTab,
            component_type: CardComponentType,
            vectorization_key: str,
            vector: List[float]
    ) -> MutationResult:
        self._init()
        return self.message_collection.insert([
            {
                "id": uuid.uuid4().hex,
                "user_id": message.user.id,
                "session_id": message.session.id,
                "msg_id": message.msg_id,
                "msg_pk": message.id,
                "component_type": component_type,
                "vectorization_key": vectorization_key,
                "vector": vector
            }
        ])

    def save_sentence(self, sentence_record: models.KnowledgeSentence, vector: List[float]) -> MutationResult:
        self._init()

        return self.knowledge_base_collection.insert([
            {
                "id": sentence_record.id,
                "raw_content": sentence_record.raw_content,
                "doc_name": sentence_record.file.filename,
                "doc_id": sentence_record.file.id,
                "vector": vector
            }
        ])

    def save_combobox_candidate(
            self, user_id: int, business_id: int,
            business_type: BusinessType, values: List[str], vectors: List[List[float]]
    ) -> MutationResult:
        self._init()

        return self.candidate_collection.insert([
            {
                "id": uuid.uuid4().hex,
                "user_id": user_id,
                "business_id": business_id,
                "type": business_type,
                "vectorization_key": value,
                "vector": vector
            } for value, vector in zip(values, vectors)
        ])

    def find_message(
            self,
            keywords: Union[List[str], str],
            component_type_list: List[CardComponentType],
            user_id: int,
            k: int = 20
    ) -> List[int]:
        self._init()
        start_time = time.time()
        log.info(
            "search messages, user_id: %s keywords: %s, component_type_list: %s",
            user_id,
            keywords,
            component_type_list
        )
        if isinstance(keywords, str):
            keywords = [keywords]
        vectors = embed_message_component(keywords)
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }
        expr = f"user_id == {user_id}"
        if component_type_list:
            expr += f" and component_type in {component_type_list}"
        search_res = self.message_collection.search(
            vectors, "vector", search_params, k, expr, None, ["msg_pk"]
        )
        res: List[Hit] = sorted(filter(lambda h: h.score < 0.42, [hit for hits in search_res for hit in hits]),
                                key=lambda h: h.score)

        log.info(
            "[VectorAccess] /find_message %.3fs result=%s",
            time.time() - start_time,
            [f"[{hit.get('msg_pk')}, {hit.score:.3f}]" for hit in res]
        )
        return [h.get("msg_pk") for h in res]

    def find_sentences(self, keywords: Union[List[str], str], doc_id_list: List[int], k: int = 5) -> List[DocSearchRes]:
        log.info("search sentences, keywords: %s, doc_id_list: %s", keywords, doc_id_list)
        self._init()

        if not doc_id_list:
            return []
        start_time = time.time()
        if isinstance(keywords, str):
            keywords = [keywords]
        vectors = embed_sentence(keywords)

        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }
        expr = f"doc_id in {doc_id_list}"
        search_res = self.knowledge_base_collection.search(
            vectors, "vector", search_params, k, expr, None, ["id", "doc_id"]
        )
        res: List[Hit] = [hit for hits in search_res for hit in hits]
        res = list(filter(lambda h: h.score < 0.35, res))
        res.sort(key=lambda h: h.score)  # distance, less is better
        res = res[:25]

        log.info(
            "[VectorAccess] /find_sentences %.3fs result=%s",
            time.time() - start_time,
            [f"[{hit.get('id')}, {hit.score:.3f}]" for hit in res]
        )
        return [DocSearchRes(**h.fields) for h in res]

    def find_combobox_candidate_value(
            self,
            keywords: Union[List[str], str],
            user_id: int,
            business_type: BusinessType,
            k: int = 50,
            max_distance: float = 1
    ) -> List[CandidateSearchRes]:
        log.info(
            "search find combobox candidate value, keywords: %s, user_id: %s, business_type: %s",
            keywords, user_id, business_type
        )
        self._init()

        start_time = time.time()
        if isinstance(keywords, str):
            keywords = [keywords]
        vectors = embed_candidate(keywords)
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }
        expr = f"type == '{business_type}' and user_id == {user_id}"
        search_res = self.candidate_collection.search(
            vectors, "vector", search_params, k, expr,
            None, ["id", "business_id", "vectorization_key"])
        res: List[Hit] = [hit for hits in search_res for hit in hits]
        res = list(filter(lambda h: h.score < max_distance, res))
        res.sort(key=lambda h: h.score)  # distance, less is better
        # res = res[:25]

        log.info(
            "[VectorAccess] /find_combobox_candidate_value %.3fs result=%s",
            time.time() - start_time,
            [f"[{hit.get('id')}, {hit.score:.3f}]" for hit in res]
        )
        return [CandidateSearchRes(**h.fields) for h in res]


vector_access = VectorAccess()
