import os
import time
from enum import Enum
from typing import List, Callable, Optional, Type, Any, Sequence, Union, Dict

from langchain.chains import LLMChain
from langchain.output_parsers.ernie_functions import PydanticOutputFunctionsParser
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import BaseLLMOutputParser
from langchain_core.outputs import Generation
from langchain_core.prompts import BasePromptTemplate, ChatPromptTemplate
from pydantic import BaseModel, Field, create_model
from pydantic.fields import Undefined

from lemon_rag.lemon_runtime import models
from lemon_rag.settings import lemon_env
from lemon_rag.utils import log


class EmbeddingModel(str, Enum):
    DEFAULT = "text-embedding-ada-002"


Embedding_F = Callable[[List[str]], List[List[float]]]


class NOOPFunc(BaseModel):
    async def execute(self, inherit_memory: Optional[ChatMessageHistory] = None) -> str:
        pass


def get_embedding_function(metrics_name: str) -> Embedding_F:
    embeddings: List[Optional[OpenAIEmbeddings]] = [None]

    def init_embeddings_client():
        if embeddings[0]:
            return
        openai_config: Optional[models.OPENAIConfig] = models.OPENAIConfig.get_or_none()
        if not openai_config:
            raise ValueError("openai_config not found")
        embeddings[0] = OpenAIEmbeddings(openai_api_base=openai_config.base_url, openai_api_key=openai_config.api_key)

    def inner(text: List[str]) -> List[List[float]]:
        init_embeddings_client()
        start_time = time.time()
        client = embeddings[0]
        time_cost = time.time() - start_time
        embedding_key_len = [len(k) for k in text]
        log.info("[Embedding] /%s %.3fs embedding_key_len: %s", metrics_name, time_cost, embedding_key_len)
        return client.embed_documents(text)

    return inner


llm: List[Optional[ChatOpenAI]] = [
    ChatOpenAI(model_name="gpt-3.5-turbo-1106", streaming=True)
    if lemon_env == "Development" and os.environ.get('OPENAI_API_KEY') else None
]


def get_llm(max_tokens: int = 700):
    if llm[0] is None:
        log.info("all openai configs: %s", list(models.OPENAIConfig.select()))
        openai_config: Optional[models.OPENAIConfig] = models.OPENAIConfig.get_or_none()
        llm[0] = ChatOpenAI(
            model_name="gpt-3.5-turbo-1106", openai_api_base=openai_config.base_url,
            openai_api_key=openai_config.api_key, streaming=True, max_tokens=700)
    return llm[0]


class OpenAIFunctionParser(PydanticOutputFunctionsParser):
    def parse_result(self, result: List[Generation], *, partial: bool = True) -> Any:
        if result[0].text:
            return result[0].text
        return super().parse_result(result)


def _get_openai_output_parser(
        functions: List[Type[BaseModel]],
        function_names: Sequence[str],
) -> BaseLLMOutputParser:
    """Get the appropriate function output parser given the user functions."""
    functions += [NOOPFunc]
    if isinstance(functions[0], type) and issubclass(functions[0], BaseModel):
        if len(functions) > 1:
            pydantic_schema: Union[Dict, Type[BaseModel]] = {
                name: fn for name, fn in zip(function_names, functions)
            }
        else:
            pydantic_schema = functions[0]
        output_parser: BaseLLMOutputParser = OpenAIFunctionParser(
            pydantic_schema=pydantic_schema
        )
    else:
        output_parser = JsonOutputFunctionsParser(args_only=len(functions) <= 1)
    return output_parser


def convert_to_openai_function(function: Type[BaseModel]):
    fields_included = {
        field.name: (field.type_, field.field_info) for field in function.__fields__.values() if
        (not field.field_info.exclude) and (field.field_info.default == Undefined)
    }

    # 动态创建新的类
    new_class = create_model(function.__class__.__name__, **fields_included)
    schema = new_class.schema()
    schema.pop("title")
    return {
        "name": function.__name__,
        "description": function.schema().get("description", ""),
        "parameters": schema,
    }


def create_openai_fn_chain(
        functions: List[Type[BaseModel]],
        llm: BaseLanguageModel,
        prompt: BasePromptTemplate,
        *,
        output_parser: Optional[BaseLLMOutputParser] = None,
        **kwargs: Any,
) -> LLMChain:
    functions = functions or []
    openai_functions = [convert_to_openai_function(f) for f in functions]
    fn_names = [oai_fn["name"] for oai_fn in openai_functions]
    output_parser = output_parser or _get_openai_output_parser(functions, fn_names)
    if openai_functions:
        kwargs.update({
            "llm_kwargs": {"functions": openai_functions},
            "output_key": "function"
        })
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        output_parser=output_parser,
        **kwargs,
    )
    return llm_chain


class ChatChain(BaseModel):
    template: ChatPromptTemplate
    llm: ChatOpenAI = Field(default_factory=get_llm)
    functions: List[Type[BaseModel]] = []

    def run(self, callbacks: Optional[List[BaseCallbackHandler]] = None, **kwargs):
        chain = create_openai_fn_chain(self.functions, self.llm, self.template, verbose=True)
        result = chain.run(
            callbacks=callbacks,
            **kwargs
        )
        return result


if __name__ == '__main__':
    f = get_embedding_function("hha")
    res = f(["你好啊"])
    print(res)
