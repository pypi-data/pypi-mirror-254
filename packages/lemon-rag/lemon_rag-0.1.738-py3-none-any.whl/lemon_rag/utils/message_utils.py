import queue
import uuid
from typing import List

from playhouse.shortcuts import model_to_dict
from sqlalchemy import Transaction

from lemon_rag.api.local import get_user
from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.protocols.chat import CardMessage, Message, FormSchema, TransactionData, Tag


def get_form_submit_notification_message(
        session: models.SessionTab, items: List[str], item_title: str
) -> Message:
    format_account_names = "\n".join(map(lambda v: f"* {v}", items))
    card = CardMessage().add_text(f"已经成功录入`{len(items)}`个{item_title}：\n{format_account_names}")
    ai_message = data_access.create_ai_message(
        get_user(),
        models.SessionTab(id=session),
        card.json(),
        uuid.uuid4().hex,
        None
    )
    return Message(**model_to_dict(ai_message))


def get_transaction_tab_tags(transaction: models.TransactionTab) -> List[Tag]:
    tags = [Tag(value=transaction.type), Tag(value=transaction.transaction_item.name)]
    if transaction.contract:
        tags.append(Tag(value=f"合同{transaction.contract.number}"))
    if transaction.project:
        tags.append(Tag(value=f"项目:{transaction.project.name}"))
    return tags


def get_receivable_payable_tab_tags(receivable_payable: models.ReceivablePayableTab) -> List[Tag]:
    tags = [Tag(value=receivable_payable.type), Tag(value=receivable_payable.project.name)]
    if receivable_payable.contract:
        tags.append(Tag(value=f"合同{receivable_payable.contract.number}"))
    if receivable_payable.product_name:
        tags.append(Tag(value=f"{receivable_payable.product_name}x{receivable_payable.quantity}"))
    if receivable_payable.project:
        tags.append(Tag(value=f"项目:{receivable_payable.project.name}"))
    return tags


def get_trx_card_message_from_transaction(
        session: models.SessionTab, transactions: List[models.TransactionTab]
):
    return get_trx_card_message(session, [
        TransactionData(
            id=t.id, trx_code=t.voucher_number, title=t.description
            , amount=t.amount, tags=get_transaction_tab_tags(t), datetime=t.date
        ) for t in transactions
    ], "收支")


def get_trx_card_message_from_receivable_payable_bills(
        session: models.SessionTab, bills: List[models.ReceivablePayableTab]
):
    return get_trx_card_message(session, [
        TransactionData(
            id=bill.id, trx_code="", title=bill.description, amount=bill.amount,
            tags=[], datetime=bill.date, datetime_label="到期时间："
        )
        for bill in bills
    ], "应收应付单")


def get_trx_card_message(
        session: models.SessionTab, transactions: List[TransactionData], title: str
):
    card = CardMessage().add_text(f"已经成功录入`{len(transactions)}`条{title}.")
    for trx in transactions:
        card.add_transaction_card(trx)
    ai_message = data_access.create_ai_message(
        get_user(),
        models.SessionTab(id=session),
        card.json(),
        uuid.uuid4().hex,
        None
    )
    return Message(**model_to_dict(ai_message))
