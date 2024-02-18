import traceback
from concurrent.futures import ThreadPoolExecutor
from typing import List, Union

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.dependencies.vector_access import vector_access, embed_sentence, embed_message_component, \
    embed_candidate
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.rag.vectorization.content_extractor import Paragraph
from lemon_rag.protocols.chat import CardMessage, BusinessType
from lemon_rag.utils import log
from lemon_rag.utils.executor_utils import submit_task

vectorization_pool = ThreadPoolExecutor(max_workers=16)


def vectorization_document(file: models.KnowledgeBaseFileTab, sentences: List[models.KnowledgeSentence]):
    log.info(
        "start vectorize the sentences of the file, id=%s, filename=%s, n_sentences=%s", file.id,
        file.origin_filename, len(sentences)
    )
    for index, sentence in enumerate(sentences):
        try:
            vectors = embed_sentence([sentence.raw_content])
            vector_access.save_sentence(sentence, vectors[0])
            rows = data_access.set_vectorized(sentence.id)
            log.info("set sentence id=%s vectorized, [%s] rows affected", sentence.id, rows)
            if index % 10 == 0:
                data_access.update_file_vectorized_count(file)
        except Exception as e:
            log.info("vectorization task error, file: %s sentence: %s, error: %s", file, sentence, traceback.format_exc())
    data_access.update_file_vectorized_count(file)


def parse_and_vectorize_document(file: models.KnowledgeBaseFileTab, paragraphs: List[Paragraph]):
    log.info("start parse the file, id=%s, filename=%s", file.id, file.origin_filename)
    paragraphs_records = data_access.create_paragraphs(file, paragraphs)
    submit_task(
        vectorization_pool,
        vectorization_document,
        file,
        list(file.sentences.where(models.KnowledgeSentence.vectorized == False))
    )


def start_parse_document(file: models.KnowledgeBaseFileTab, paragraphs: List[Paragraph]):
    parse_and_vectorize_document(file, paragraphs)


def vectorize_message(message: models.MessageTab, card: CardMessage) -> None:
    for component in card.components:
        for embed_key in component.embed_keys():
            if not embed_key:
                continue
            vectors = embed_message_component([embed_key])
            vector_access.save_message(message, component.type, embed_key, vectors[0])


def vectorize_candidate(
        user_id: int, business_id: int, business_type: BusinessType, embed_key: Union[str, List[str]]
) -> None:
    if isinstance(embed_key, str):
        embed_key = [embed_key]
    vectors = embed_candidate(embed_key)
    vector_access.save_combobox_candidate(user_id, business_id, business_type, embed_key, vectors)
