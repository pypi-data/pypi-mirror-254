import re
from typing import List, Union

from lemon_rag.dependencies.vector_access import vector_access, CandidateSearchRes
from lemon_rag.lemon_runtime import models
from lemon_rag.protocols.chat import BusinessType


def retrieve_candidate(
        query: Union[str, List[str]],
        business_type: BusinessType,
        user: models.AuthUserTab,
        k: int = 50
) -> List[CandidateSearchRes]:
    if isinstance(query, str):
        query = [query]
    keys: List[str] = []
    for q in query:
        keys.extend(list(filter(lambda key: key.strip(), re.split(r",.，。\n", q))))
    return vector_access.find_combobox_candidate_value(keys, user.id, business_type, k)
