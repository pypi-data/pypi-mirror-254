import queue

from pydantic import Field

from lemon_rag.dependencies.data_access import data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.interactive_functions.base_function import ToolFunction
from lemon_rag.llm.agents.prompts.form_record import form_record_chat
from lemon_rag.protocols.business_form import get_form_schema_by_type
from lemon_rag.protocols.chat import CardMessage, BusinessDataType, FormSchema
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import get_chat_context_history


class FormDataRecord(ToolFunction):
    """Call this function to record form data. Before calling function, You need to ensure that the record data contains corresponding information: transaction(account name, transaction category, amount, project name, contract number), employee(employee name, age, gender), project(project name, employee name, start date, end date), account(account name, amount)"""

    type: BusinessDataType = Field(description=f"You can choose {'/'.join(BusinessDataType)}")

    def execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        form_field_schema = get_form_schema_by_type(self.type)

        session = data_access.get_session_by_id(ai_message.session.id)
        chat_context = get_chat_context_history(session, text_only=True)

        form_data_result = form_record_chat(chat_context, form_field_schema, ai_message, q, card)
        log.info("finally form data result: %s", form_data_result)
        return ""

    # * internal transfer: source account, target account, amount
    # * receivable payable: type, handler, contract number, quantity, unit_price, end date
    # * employee loan: employee name, amount, end date
    # * employee salary: employee name, amount
    # * contract: number, contract name, project name, type, customer name, supplier name, amount, end date
    # * invoice: contract number, amount


class BaseFormTool(ToolFunction):
    type: BusinessDataType

    def execute(self, q: queue.Queue, ai_message: models.MessageTab, user_requirement: str, card: CardMessage) -> str:
        form_field_schema = get_form_schema_by_type(self.type)

        session = data_access.get_session_by_id(ai_message.session.id)
        chat_context = get_chat_context_history(session, text_only=True)

        form_data_result = form_record_chat(chat_context, form_field_schema, ai_message, q, card)
        log.info("finally form data result: %s", form_data_result)
        return ""


def join_required_fields(form_schema: FormSchema):
    return ",".join(f.name for f in form_schema.fields if f.required)


class CreateNewEmployee(BaseFormTool):
    """create/insert new employees"""
    type: BusinessDataType = Field(BusinessDataType.employee, exclude=True)
    employees: str


class CreateNewProject(BaseFormTool):
    """create/record new projects"""
    type: BusinessDataType = Field(BusinessDataType.project, exclude=True)
    projects: str


class CreatePaymentAccount(BaseFormTool):
    """create payment accounts"""
    type: BusinessDataType = Field(BusinessDataType.account, exclude=True)
    account_name: str
    balance: int


class CreateNewInvoice(BaseFormTool):
    """create new invoices"""
    type: BusinessDataType = Field(BusinessDataType.invoice, exclude=True)


class CreateNewContract(BaseFormTool):
    """create new purchase/sale/project contracts"""
    type: BusinessDataType = Field(BusinessDataType.contract, exclude=True)


class RecordSalaryBill(BaseFormTool):
    """record employee's salary bill"""
    type: BusinessDataType = Field(BusinessDataType.employee_salary, exclude=True)


class RecordAdvanceBill(BaseFormTool):
    """record advancing money to the employees for business usage."""
    type: BusinessDataType = Field(BusinessDataType.employee_loan, exclude=True)
    amount: int
    usage: str
    employee: str


class RecordReceivablePayableBill(BaseFormTool):
    """record receivable payable bills"""
    type: BusinessDataType = Field(BusinessDataType.receivable_payable, exclude=True)
    amount: int
    project: str


class RecordInternalTransfer(BaseFormTool):
    """record internal transfer between internal accounts"""
    type: BusinessDataType = Field(BusinessDataType.internal_transfer, exclude=True)
    amount: int
    source_account: str
    target_account: str


class RecordTransaction(BaseFormTool):
    """Record the actual incoming and expense"""
    type: BusinessDataType = Field(BusinessDataType.transaction, exclude=True)
    payment_account: str
    usage: str
    amount: int


class CreateNewSupplier(BaseFormTool):
    """create new suppliers, supplier should be a company"""
    type: BusinessDataType = Field(BusinessDataType.supplier, exclude=True)
    name: str
    mobile_number: str


class CreateNewCustomer(BaseFormTool):
    """create new customers"""
    type: BusinessDataType = Field(BusinessDataType.customer, exclude=True)
    name: str
    mobile_number: str
