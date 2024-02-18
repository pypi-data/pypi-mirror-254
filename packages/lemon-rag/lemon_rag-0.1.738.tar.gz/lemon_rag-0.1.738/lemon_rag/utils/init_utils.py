import time
from datetime import datetime

from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.rag.vectorization.runner import vectorization_pool, vectorize_candidate
from lemon_rag.protocols.business_form import TransactionItem
from lemon_rag.protocols.chat import BusinessType
from lemon_rag.utils.executor_utils import submit_task


def init_transaction_item(creator: models.AuthUserTab):
    for item in TransactionItem:
        transaction_item = models.TransactionItemTab.create(**{
            "name": item.value,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

        submit_task(
            vectorization_pool, vectorize_candidate,
            creator.id, transaction_item.id, BusinessType.transaction_item, transaction_item.name
        )
