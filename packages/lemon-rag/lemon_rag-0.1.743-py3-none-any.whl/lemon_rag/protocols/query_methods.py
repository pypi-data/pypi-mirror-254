import datetime
import queue
from abc import abstractmethod
from typing import List, Type, Optional, Any, TypeVar

import peewee
from pydantic import Field

from lemon_rag.api.local import get_user
from lemon_rag.dependencies.data_access import business_data_access
from lemon_rag.dependencies.vector_access import vector_access, CandidateSearchRes
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.interactive_functions.base_function import ToolFunction
from lemon_rag.protocols.business_enum import GenderType, TransactionItem, TransactionType, ReceivablePayableType
from lemon_rag.protocols.chat import CardMessage, ResponseChunk, BusinessType, ProjectCardData, Member, TransactionData
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import get_send_text_message_function, get_business_db_cls_by_type
from lemon_rag.utils.message_utils import get_transaction_tab_tags, get_receivable_payable_tab_tags
from lemon_rag.utils.time_format import extract_time_range

T = TypeVar('T', bound=models.BaseModel)


def sort_by_id_list(items: List[T], res: List[CandidateSearchRes]):
    if not res:
        return
    id_to_index_mapping = {v.business_id: index for index, v in enumerate(res)}
    log.info('id_to_index_mapping: %s', id_to_index_mapping)
    items.sort(key=lambda v: id_to_index_mapping.get(v.id, 0))


class DataQueryToolWrapper(ToolFunction):
    default_query_max_distance = Field(0.35, exclude=True)

    @abstractmethod
    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        pass

    def execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        log.info("[DataQuery] %s %s", self.__class__.__name__, self.json())
        self._execute(q, ai_message, user_requirement, card)
        q.put(ResponseChunk.add_button(
            ai_message.session.id, ai_message.msg_id, "", [], card
        ).json())
        return ""


class FindEmployees(DataQueryToolWrapper):
    """query employee data"""
    # TODO: 参数字段映射到查询条件，而不是动态手动拼接参数
    employee_names: str = Field(description="names split by ,")
    gender: str = Field(description='|'.join(GenderType))

    def get_employee_card_description(self) -> str:
        desc = ['将为你查询']
        if self.gender:
            desc.append(f'年龄为`{self.gender}`')
        if self.employee_names:
            desc.append(f'姓名为`{self.employee_names}`')
        if len(desc) == 1:
            desc.append('全部')
        desc.append(f'的员工信息')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_employee_card_description())
        names = list(filter(bool, self.employee_names.split(",")))
        conditions: List[Any] = []
        vector_res: Optional[List[CandidateSearchRes]] = None
        if names:
            res = vector_access.find_combobox_candidate_value(
                names, get_user(), business_type=BusinessType.employee, max_distance=0.25
            )
            conditions.append(models.EmployeeTab.id.in_([r.business_id for r in res]))
            vector_res = res
        if self.gender:
            conditions.append(models.EmployeeTab.gender == self.gender)

        employees = list(business_data_access.list_data_by_cls_creator(
            get_business_db_cls_by_type(BusinessType.employee), get_user(), conditions))
        sort_by_id_list(employees, vector_res)
        if not employees:
            send_text("\n未筛选到符合条件的员工数据\n", append=False)
        else:
            send_text("\n筛选到符合条件的员工数据\n", append=False)
        for employee in employees:
            q.put(ResponseChunk.add_text(
                ai_message.session.id, ai_message.msg_id,
                f"* 姓名：`{employee.name}` 年龄：`{employee.age}` 性别：`{employee.gender}`\n", card
            ).json())
        return ""


def get_project_data(project: models.ProjectTab) -> ProjectCardData:
    now = datetime.datetime.now()
    days_remained = (datetime.datetime.strptime(project.end_date, "%Y年%m月%d日").date() - now.date()).days
    total_stage = business_data_access.count_payable_receivable_bills_by_project_and_status(
        project, get_user(), ReceivablePayableType.RECEIVABLE,
    )
    finished_stages = business_data_access.count_payable_receivable_bills_by_project_and_status(
        project, get_user(), ReceivablePayableType.RECEIVABLE, True
    )
    members = business_data_access.get_project_members(project)
    incoming = business_data_access.get_project_transaction_amount_sum(project, type_=TransactionType.INCOME)
    out_coming = business_data_access.get_project_transaction_amount_sum(project, type_=TransactionType.EXPENSE)
    return ProjectCardData(
        id=project.id, name=project.name, days_remained=days_remained, total_stage=total_stage,
        current_stage=finished_stages, members=[Member(id=m.id, name=m.name, avatar="") for m in members],
        incoming=incoming, out_coming=out_coming, balance=project.budget - out_coming
    )


class FindProjects(DataQueryToolWrapper):
    """query projects by name, end time or the charger"""

    project_names: str = Field(description="names split by ,")
    end_time_range: str = Field(description="range of end date")
    charger: str = Field(description="charger employee name")

    def get_project_card_description(self) -> str:
        desc = ['将为你查询']
        if self.project_names:
            desc.append(f'项目名称为`{self.project_names}`')
        if self.end_time_range:
            desc.append(f'结束时间在`{self.end_time_range}`范围内')
        if self.charger:
            desc.append(f'负责人为`{self.charger}`')
        if len(desc) == 1:
            desc.append('全部')
        desc.append(f'的项目信息')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_project_card_description())
        names = list(filter(bool, self.project_names.split(",")))
        conditions: List[Any] = [models.ProjectTab.creator == get_user()]
        query = models.ProjectTab.select()
        vector_res: Optional[List[CandidateSearchRes]] = None

        if names:
            res = vector_access.find_combobox_candidate_value(
                names, get_user(), business_type=BusinessType.project, max_distance=self.default_query_max_distance
            )
            conditions.append(models.ProjectTab.id.in_([r.business_id for r in res]))
            vector_res = res
        if self.end_time_range:
            start_time, end_time = extract_time_range(self.end_time_range)
            if start_time:
                conditions.append(models.ProjectTab.end_date >= start_time)
            if end_time:
                conditions.append(models.ProjectTab.end_date <= end_time)

        if self.charger:
            res = vector_access.find_combobox_candidate_value(
                self.charger, get_user(), business_type=BusinessType.employee, max_distance=0.2, k=1
            )
            if res:
                query = query.join(models.EmployeeProjectRecord)
                conditions.append(models.EmployeeProjectRecord.is_leader == True)
                conditions.append(models.EmployeeProjectRecord.employee == models.EmployeeTab(id=res[0].business_id))
        projects = list(query.where(*conditions))
        sort_by_id_list(projects, vector_res)
        if not projects:
            send_text("\n未筛选到符合条件的项目：\n", append=False)
        else:
            send_text("\n筛选到符合条件的项目：\n", append=False)
        for project in projects:
            q.put(ResponseChunk.add_project_card(
                ai_message.session.id, ai_message.msg_id, get_project_data(project), card).json())
        return ""


class FindPaymentAccount(DataQueryToolWrapper):
    """query existed payment account"""

    account_names: str = Field(description="names split by ,")
    min_balance: int = Field(description="the lower limit for filtering account amount")
    max_balance: int = Field(description="the upper limit for filtering account amount")

    def get_account_card_description(self) -> str:
        desc = ['将为你查询']
        if self.account_names:
            desc.append(f'账户名称为`{self.account_names}`')
        if self.min_balance is not None and self.max_balance is not None:
            desc.append(f'账户余额在`{self.min_balance}`和`{self.max_balance}`之间')
        elif self.min_balance is not None:
            desc.append(f'账户余额不低于`{self.min_balance}`')
        elif self.max_balance is not None:
            desc.append(f'账户余额不高于`{self.max_balance}`')
        else:
            desc.append('全部')
        desc.append('的支付账户信息')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_account_card_description())

        account_names = list(filter(bool, self.account_names.split(",")))
        conditions: List[Any] = []
        vector_res: Optional[List[CandidateSearchRes]] = None

        if account_names:
            vector_res = vector_access.find_combobox_candidate_value(
                account_names, get_user(), business_type=BusinessType.account,
                max_distance=self.default_query_max_distance
            )
            conditions.append(models.AccountTab.id.in_([r.business_id for r in vector_res]))

        if self.min_balance:
            conditions.append(models.AccountTab.amount >= self.min_balance)

        if self.max_balance:
            conditions.append(models.AccountTab.amount <= self.max_balance)

        accounts = list(business_data_access.list_data_by_cls_creator(
            get_business_db_cls_by_type(BusinessType.account), get_user(), conditions))
        sort_by_id_list(accounts, vector_res)
        if not accounts:
            send_text("\n未筛选到符合条件的账户数据\n", append=False)
        else:
            send_text("\n筛选到符合条件的账户数据\n", append=False)

        for account in accounts:
            q.put(ResponseChunk.add_text(
                ai_message.session.id, ai_message.msg_id,
                f"* 账户名称：`{account.name}` 金额：`{round(account.amount, 2)}`\n",
                card
            ).json())
        return ""


class QueryCustomer(DataQueryToolWrapper):
    """find customers by names, phone number"""

    customer_names: str = Field(description="customer names split by ,")
    phone_number: str = Field(description="customer contact phone number")

    def get_customer_card_description(self) -> str:
        desc = ['将为你查询']
        if self.customer_names:
            desc.append(f'姓名为`{self.customer_names}`')
        if self.phone_number:
            desc.append(f'联系电话为`{self.phone_number}`')
        if len(desc) == 1:
            desc.append('全部')
        desc.append(f'的客户信息')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_customer_card_description())
        customer_names = list(filter(bool, self.customer_names.split(",")))
        conditions: List[Any] = []
        vector_res: Optional[List[CandidateSearchRes]] = None

        if customer_names:
            vector_res = vector_access.find_combobox_candidate_value(
                customer_names, get_user(), business_type=BusinessType.customer,
                max_distance=self.default_query_max_distance
            )
            conditions.append(models.CustomerTab.id.in_([r.business_id for r in vector_res]))

        if self.phone_number:
            conditions.append(models.CustomerTab.contact_phone == self.phone_number)

        customers = list(business_data_access.list_data_by_cls_creator(
            get_business_db_cls_by_type(BusinessType.customer), get_user(), conditions))
        sort_by_id_list(customers, vector_res)
        if not customers:
            send_text("\n未筛选到符合条件的客户数据\n", append=False)
        else:
            send_text("\n筛选到符合条件的客户数据\n", append=False)

        for customer in customers:
            q.put(ResponseChunk.add_text(
                ai_message.session.id, ai_message.msg_id,
                f"* 客户名称：`{customer.name}` 联系人：`{customer.contact_name}` 联系电话：`{customer.contact_phone}`\n",
                card
            ).json())
        return ""


class QuerySuppliers(DataQueryToolWrapper):
    """find suppliers by names, phone number"""

    supplier_names: str = Field(description="supplier names split by ,")
    phone_number: str = Field(description="supplier contact phone number")

    def get_supplier_card_description(self) -> str:
        desc = ['将为你查询']
        if self.supplier_names:
            desc.append(f'供应商名称为`{self.supplier_names}`')
        if self.phone_number:
            desc.append(f'联系电话为`{self.phone_number}`')
        if len(desc) == 1:
            desc.append('全部')
        desc.append(f'的供应商信息')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_supplier_card_description())
        supplier_names = list(filter(bool, self.supplier_names.split(",")))
        conditions: List[Any] = []
        vector_res: Optional[List[CandidateSearchRes]] = None

        if supplier_names:
            vector_res = vector_access.find_combobox_candidate_value(
                supplier_names, get_user(), business_type=BusinessType.supplier,
                max_distance=self.default_query_max_distance
            )
            conditions.append(models.SupplierTab.id.in_([r.business_id for r in vector_res]))

        if self.phone_number:
            conditions.append(models.SupplierTab.contact_phone == self.phone_number)

        suppliers = list(business_data_access.list_data_by_cls_creator(
            get_business_db_cls_by_type(BusinessType.supplier), get_user(), conditions))
        sort_by_id_list(suppliers, vector_res)
        if not suppliers:
            send_text("\n未筛选到符合条件的供应商数据\n", append=False)
        else:
            send_text("\n筛选到符合条件的供应商数据\n", append=False)
        for supplier in suppliers:
            q.put(ResponseChunk.add_text(
                ai_message.session.id, ai_message.msg_id,
                f"* 供应商名称：`{supplier.name}` 联系人：`{supplier.contact_name}` 联系电话：`{supplier.contact_phone}`\n",
                card
            ).json())
        return ""


def get_transaction_data_or_bill_data(data: peewee.Model) -> Optional[TransactionData]:
    if isinstance(data, models.TransactionTab):
        return TransactionData(
            id=data.id, trx_code=data.voucher_number, title=data.description
            , amount=data.amount, tags=get_transaction_tab_tags(data), datetime=data.date
        )
    if isinstance(data, models.ReceivablePayableTab):
        return TransactionData(
            id=data.id, trx_code="", title=data.description, amount=data.amount,
            tags=get_receivable_payable_tab_tags(data), datetime=data.end_date
        )
    return None


class QueryTransactions(DataQueryToolWrapper):
    """find transactions by project, account, usage, type, date range"""

    project_names: str = Field(description="project names split by ,")
    account_names: str = Field(description="transaction account names split by ,")
    usage: str = Field(description='|'.join(TransactionItem))
    type: str = Field(description='|'.join(TransactionType))
    date_range: str = Field(description="date range")

    def get_transaction_card_description(self) -> str:
        desc = ['将为你查询']
        if self.project_names:
            desc.append(f'`{self.project_names}`项目的')
        if self.account_names:
            desc.append(f'账户为`{self.account_names}`')
        if self.usage:
            desc.append(f'用途为`{self.usage}`')
        if self.type:
            desc.append(f'类型为`{self.type}`')
        if self.date_range:
            desc.append(f'日期范围为`{self.date_range}`')
        if len(desc) == 1:
            desc.append('全部')
        desc.append(f'的交易信息')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_transaction_card_description())

        query = models.TransactionTab.select()
        conditions: List[Any] = [models.TransactionTab.creator == get_user()]
        related_model: List[Type[peewee.Model]] = []
        project_names = list(filter(bool, self.project_names.split(",")))

        if project_names:
            res = vector_access.find_combobox_candidate_value(
                project_names, get_user(), business_type=BusinessType.project,
                max_distance=self.default_query_max_distance
            )
            related_model.append(models.ProjectTab)
            conditions.append(models.ProjectTab.id.in_([r.business_id for r in res]))

        account_names = list(filter(bool, self.account_names.split(",")))
        if account_names:
            res = vector_access.find_combobox_candidate_value(
                account_names, get_user(), business_type=BusinessType.account,
                max_distance=self.default_query_max_distance
            )
            if res:
                related_model.append(models.AccountTab)
                conditions.append(models.AccountTab.id.in_([r.business_id for r in res]))

        if self.usage:
            transaction_item = business_data_access.get_transaction_item_by_name(self.usage, get_user())
            if transaction_item:
                conditions.append(models.TransactionTab.transaction_item == transaction_item)

        if self.type:
            conditions.append(models.TransactionTab.type == self.type)

        if self.date_range:
            start_time, end_time = extract_time_range(self.date_range)
            if start_time:
                conditions.append(models.TransactionTab.date >= start_time)
            if end_time:
                conditions.append(models.TransactionTab.date <= end_time)

        # 查询
        if related_model:
            query = query.join(*related_model)
        transactions = list(query.where(*conditions).execute())

        if not transactions:
            send_text("\n未筛选到符合条件的收支记录：\n", append=False)
        else:
            send_text("\n筛选到符合条件的收支记录：\n", append=False)
        for transaction in transactions:
            q.put(ResponseChunk.add_transaction_card(
                ai_message.session.id, ai_message.msg_id,
                get_transaction_data_or_bill_data(transaction), card).json())
        return ""


class QueryPayableOrReceivableBills(DataQueryToolWrapper):
    """find payable or receivable bills by project, due date, paid status"""
    bill_descriptions: str = Field(description="the description of payable/receivable bill split ,")
    project_names: str = Field(description="project names split ,")
    date_range: str = Field(description="date range")
    is_write_off: Optional[bool] = Field(description="indicates whether the bill has been written off or not")
    type: str = Field(description=f"{'|'.join(ReceivablePayableType)}")

    def get_bill_card_description(self) -> str:
        desc = ['将为你查询']
        bill_type = '应收单' if self.type == ReceivablePayableType.RECEIVABLE else '应付单'
        if self.project_names:
            desc.append(f'`{self.project_names}项目的`')
        if self.bill_descriptions:
            desc.append(f'关于`{self.bill_descriptions}`的')
        if self.date_range:
            desc.append(f'日期范围为`{self.date_range}`')
        if self.is_write_off is not None:
            if self.is_write_off:
                desc.append(f'已核销')
            else:
                desc.append(f'未核销')
        if len(desc) == 1:
            desc.append('全部')
        desc.append(f'{bill_type}')
        return '.'.join(desc)

    def _execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        send_text = get_send_text_message_function(q, ai_message.session.id, ai_message.msg_id, card)
        send_text(self.get_bill_card_description())

        query = models.ReceivablePayableTab.select()
        conditions: List[Any] = [models.ReceivablePayableTab.creator == get_user()]
        related_model: List[Type[peewee.Model]] = []

        bills = list(filter(bool, self.bill_descriptions.split(",")))
        if bills:
            res = vector_access.find_combobox_candidate_value(
                bills, get_user(), business_type=BusinessType.receivable_payable,
                max_distance=self.default_query_max_distance
            )
            conditions.append(models.ReceivablePayableTab.id.in_([r.business_id for r in res]))

        project_names = list(filter(bool, self.project_names.split(",")))
        if project_names:
            res = vector_access.find_combobox_candidate_value(
                project_names, get_user(), business_type=BusinessType.project,
                max_distance=self.default_query_max_distance
            )
            if res:
                related_model.append(models.ProjectTab)
                conditions.append(models.ProjectTab.id.in_([r.business_id for r in res]))

        if self.date_range:
            start_time, end_time = extract_time_range(self.date_range)
            if start_time:
                conditions.append(models.ReceivablePayableTab.end_date >= start_time)
            if end_time:
                conditions.append(models.ReceivablePayableTab.end_date <= end_time)

        if self.type in list(ReceivablePayableType):
            conditions.append(models.ReceivablePayableTab.type == self.type)

        if self.is_write_off is not None:
            conditions.append(models.ReceivablePayableTab.write_off == self.is_write_off)

        # 查询
        if related_model:
            query = query.join(*related_model)
        receivable_payable_bills = list(query.where(*conditions).execute())

        type_str = '应收应付' if self.type not in list(ReceivablePayableType) else self.type
        if not receivable_payable_bills:
            send_text(
                f"\n未筛选到符合条件的{type_str}记录：\n", append=False)
        else:
            send_text(f"\n筛选到符合条件的{type_str}记录：\n", append=False)
        for receivable_payable_bill in receivable_payable_bills:
            q.put(ResponseChunk.add_transaction_card(
                ai_message.session.id, ai_message.msg_id,
                get_transaction_data_or_bill_data(receivable_payable_bill), card).json())
        return ""


"""
FindEmployees '<names split by ,>' '<gender>'
FindProjects '<project names>' '<range of project end date>'
FindAccount '<account_names>' '<min_balance>' '<max_balance>'
FindCustomer '<customer title>'
FindSupplier '<supplier title>'
RaiseError '<reason>'
FindTransaction '<range of date>' '<projects split by ,>' '<incoming | out_coming>'
FindPayableInvoice '<range of due date>' '<projects split by ,>' '<suppliers split by ,>'
FindReceivableInvoice '<range of due date>' '<projects split by ,>' '<customers split by,>'
"""
query_functions: List[Type[ToolFunction]] = [
    FindEmployees, FindProjects, FindPaymentAccount, QueryCustomer, QuerySuppliers, QueryTransactions,
    QueryPayableOrReceivableBills
]
