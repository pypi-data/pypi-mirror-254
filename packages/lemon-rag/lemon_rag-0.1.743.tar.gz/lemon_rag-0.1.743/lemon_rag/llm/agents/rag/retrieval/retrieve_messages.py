import re
from typing import List

from lemon_rag.dependencies.vector_access import vector_access
from lemon_rag.lemon_runtime import models
from lemon_rag.protocols.chat import CardComponentType


def retrieve_messages(
        query: str,
        component_type_list: List[CardComponentType],
        user: models.AuthUserTab,
        k: int = 20
) -> List[int]:
    keys = list(filter(lambda key: key.strip(), re.split(r",.，。\n", query)))
    return vector_access.find_message(keys, component_type_list, user.id, k)
