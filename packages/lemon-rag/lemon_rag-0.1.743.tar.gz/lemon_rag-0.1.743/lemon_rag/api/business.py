import decimal
from typing import List, Optional

from pydantic import BaseModel, Field

from lemon_rag.api.base import handle_chat_auth, handle_request_with_pydantic, add_route
from lemon_rag.api.local import get_user
from lemon_rag.llm.agents.rag.retrieval.retrieve_candidate import retrieve_candidate
from lemon_rag.llm.agents.rag.vectorization.runner import vectorization_pool, vectorize_candidate
from lemon_rag.protocols.business import PaymentAccount, EmployeeInfo, ProjectInfo, InternalTransferRecord, \
    ContractInfo, InvoiceInfo, SalaryBill, LoanBill, ReceivablePayableBill, CustomerInfo, SupplierInfo, \
    TransactionRecord
from lemon_rag.protocols.business_enum import GenderType
from lemon_rag.protocols.chat import BusinessType, OptionPair, FormValidationError, Dependency
from lemon_rag.utils.api_utils import list_combobox_candidate_from_db_by_type, update_message_after_save_form, \
    get_business_db_cls_by_type, get_combobox_candidate_from_db_by_id_dependencies
from lemon_rag.utils.business_save_utils import project_save_event, internal_transfer_save_event, \
    contract_save_event, internal_transfer_save_before_validate, project_save_before_validate, \
    contract_save_before_validate, invoice_save_before_validate, invoice_save_event, salary_save_before_validate, \
    salary_save_event, account_save_before_validate, employee_save_before_validate, employee_loan_save_before_validate, \
    employee_loan_save_event, receivable_payable_save_before_validate, receivable_payable_save_event, \
    account_save_event, employee_save_event, customer_save_before_validate, customer_save_event, \
    supplier_save_before_validate, supplier_save_event, transaction_save_before_validate, transaction_save_event
from lemon_rag.utils.executor_utils import submit_task
from lemon_rag.dependencies.data_access import business_data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.protocols.business_form import get_form_schema_by_type
from lemon_rag.protocols.chat import Form, Message
from lemon_rag.utils.message_utils import get_form_submit_notification_message, get_trx_card_message_from_transaction, \
    get_trx_card_message_from_receivable_payable_bills
from lemon_rag.utils.response_utils import response, ErrorCodes


# def extract_number(amount_text: str) -> float:
#     pattern = r'[-+]?\d*\.\d+|\d+'
#     match = re.search(pattern, amount_text)
#     if match:
#         amount = float(match.group())
#         return amount
#     else:
#         return 0

# TODO 支持切换表单shcema，直接针对shcama做提取

class SaveFormInfoRequest(BaseModel):
    msg_id: int
    session_id: int
    forms: List[Form]


class SaveFormInfoResponse(BaseModel):
    errors: List[FormValidationError] = []
    messages: List[Message] = []


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_account_info(request: SaveFormInfoRequest):
    errors = account_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_account_names: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        account_value_map = form_schema.to_db_value_map(form.data)
        account_info = PaymentAccount(**account_value_map)
        account = account_save_event(account_info, get_user())
        saved_account_names.append(account.name)
        submit_task(
            vectorization_pool, vectorize_candidate, get_user().id, account.id, BusinessType.account, account.name)

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_account_names,
            item_title="账户"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_employee_info(request: SaveFormInfoRequest):
    errors = employee_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_employee_names: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        employee_value_map = form_schema.to_db_value_map(form.data)
        employee_info = EmployeeInfo(**employee_value_map)
        employee = employee_save_event(employee_info, get_user())
        saved_employee_names.append(employee.name)
        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, employee.id, BusinessType.employee, employee.name
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_employee_names,
            item_title="员工"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_project_info(request: SaveFormInfoRequest):
    errors = project_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_project_names: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        project_value_map = form_schema.to_db_value_map(form.data)
        project_info = ProjectInfo(**project_value_map)
        project = project_save_event(project_info, get_user())
        saved_project_names.append(project.name)
        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, project.id, BusinessType.project, project.name
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_project_names,
            item_title="项目"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_internal_transfer_record(request: SaveFormInfoRequest):
    errors = internal_transfer_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_internal_transfer_desc: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        internal_transfer_value_map = form_schema.to_db_value_map(form.data)
        internal_transfer_record = InternalTransferRecord(**internal_transfer_value_map)
        it = internal_transfer_save_event(internal_transfer_record, get_user())
        saved_internal_transfer_desc.append(
            f"{it.source_account.name}->{it.target_account.name}, 完成转账：{round(it.amount, 2)}")

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_internal_transfer_desc,
            item_title="内部转账记录"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_transaction_record(request: SaveFormInfoRequest):
    errors = transaction_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_transactions: List[models.TransactionTab] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        transaction_value_map = form_schema.to_db_value_map(form.data)
        transaction_record = TransactionRecord(**transaction_value_map)
        transaction = transaction_save_event(transaction_record, get_user())
        saved_transactions.append(transaction)

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_trx_card_message_from_transaction(models.SessionTab(id=request.session_id), saved_transactions)
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_contract_info(request: SaveFormInfoRequest):
    errors = contract_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_contract_names: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        contract_value_map = form_schema.to_db_value_map(form.data)
        contract_info = ContractInfo.create_contract(contract_value_map)
        contract = contract_save_event(contract_info, get_user())
        saved_contract_names.append(contract.name)
        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, contract.id, BusinessType.contract, [contract.number, contract.name]
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_contract_names,
            item_title="合同"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_invoice_info(request: SaveFormInfoRequest):
    errors = invoice_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_invoice_numbers: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        invoice_value_map = form_schema.to_db_value_map(form.data)
        invoice_info = InvoiceInfo(**invoice_value_map)
        invoice = invoice_save_event(invoice_info, get_user())
        saved_invoice_numbers.append(invoice.number)

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_invoice_numbers,
            item_title="发票"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_customer_info(request: SaveFormInfoRequest):
    errors = customer_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_customer_names: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        customer_value_map = form_schema.to_db_value_map(form.data)
        customer_info = CustomerInfo(**customer_value_map)
        customer = customer_save_event(customer_info, get_user())
        saved_customer_names.append(customer.name)

        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, customer.id, BusinessType.customer, customer.name
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_customer_names,
            item_title="客户"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_supplier_info(request: SaveFormInfoRequest):
    errors = supplier_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_supplier_names: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        supplier_value_map = form_schema.to_db_value_map(form.data)
        supplier_info = SupplierInfo(**supplier_value_map)
        supplier = supplier_save_event(supplier_info, get_user())
        saved_supplier_names.append(supplier.name)

        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, supplier.id, BusinessType.supplier, supplier.name
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_supplier_names,
            item_title="客户"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_employee_salary_bill(request: SaveFormInfoRequest):
    errors = salary_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_salary_desc: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        salary_value_map = form_schema.to_db_value_map(form.data)
        salary_bill = SalaryBill(**salary_value_map)
        salary = salary_save_event(salary_bill, get_user())
        saved_salary_desc.append(
            f"`{salary.employee.name}`在`{salary_bill.start_date}`至`{salary_bill.end_date}`"
            f"`{salary_bill.description}`的工资，"
            f"共`{max(salary.payable_amount - salary.deductible_amount - salary.personal_tax, decimal.Decimal('0'))}`元")
        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, salary.id, BusinessType.salary, salary.description
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_salary_desc,
            item_title="员工工资单"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_employee_loan_bill(request: SaveFormInfoRequest):
    errors = employee_loan_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_loan_desc: List[str] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        loan_value_map = form_schema.to_db_value_map(form.data)
        loan_bill = LoanBill(**loan_value_map)
        employ_loan, is_create = employee_loan_save_event(loan_bill, get_user())
        saved_loan_desc.append(employ_loan.description)
        if not is_create:
            submit_task(
                vectorization_pool, vectorize_candidate,
                get_user().id, employ_loan.id, BusinessType.employee_loan, employ_loan.description
            )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_form_submit_notification_message(
            models.SessionTab(id=request.session_id),
            items=saved_loan_desc,
            item_title="员工借款单"
        )
    ]))


@handle_chat_auth
@handle_request_with_pydantic(SaveFormInfoRequest)
def save_receivable_payable_bill(request: SaveFormInfoRequest):
    errors = receivable_payable_save_before_validate(request.forms, get_user())
    if errors:
        return response(data=SaveFormInfoResponse(errors=errors))
    saved_receivable_payable_bills: List[models.ReceivablePayableTab] = []
    for form in request.forms:
        form_schema = get_form_schema_by_type(form.type)
        receivable_payable_value_map = form_schema.to_db_value_map(form.data)
        receivable_payable_bill = ReceivablePayableBill(**receivable_payable_value_map)
        receivable_payable = receivable_payable_save_event(receivable_payable_bill, get_user())
        saved_receivable_payable_bills.append(receivable_payable)
        submit_task(
            vectorization_pool, vectorize_candidate,
            get_user().id, receivable_payable.id, BusinessType.employee_loan, receivable_payable.description
        )

    update_message_after_save_form(request.msg_id, request.session_id, request.forms)
    return response(data=SaveFormInfoResponse(messages=[
        get_trx_card_message_from_receivable_payable_bills(
            models.SessionTab(id=request.session_id), saved_receivable_payable_bills
        )
    ]))


class GetComboboxCandidateRequest(BaseModel):
    keyword: str
    type: BusinessType
    dependencies: List[Dependency] = Field(default_factory=list)


class NewOption(GetComboboxCandidateRequest):
    pass


class GetComboboxCandidateResponse(BaseModel):
    options: List[OptionPair]
    new_option: Optional[NewOption]


@handle_chat_auth
@handle_request_with_pydantic(GetComboboxCandidateRequest)
def get_combobox_candidate(request: GetComboboxCandidateRequest):
    candidates = ((retrieve_candidate(request.keyword, request.type, get_user()) if request.keyword else None) or
                  list_combobox_candidate_from_db_by_type(request.type, get_user()))
    options: List[OptionPair] = []
    is_new: bool = True
    creatable_type: List[BusinessType] = [
        BusinessType.transaction_item, BusinessType.supplier, BusinessType.customer, BusinessType.employee]
    for c in candidates:
        if candidate := get_combobox_candidate_from_db_by_id_dependencies(
                request.type, c.business_id, request.dependencies, get_user()):
            if c.vectorization_key in request.keyword:
                is_new = False
            if candidate not in options:
                options.append(candidate)
    return response(data=GetComboboxCandidateResponse(options=options, new_option=NewOption(
        keyword=request.keyword, type=request.type,
        dependencies=request.dependencies) if is_new and request.type in creatable_type else None))


class QuickCreateCandidateRequest(GetComboboxCandidateRequest):
    pass


@handle_chat_auth
@handle_request_with_pydantic(QuickCreateCandidateRequest)
def quick_create_candidate(request: QuickCreateCandidateRequest):
    if request.type == BusinessType.transaction_item:
        # TODO 有一个transaction_item枚举枚举的值可以在新手指引的时候创建
        data = business_data_access.create_transaction_item(request.keyword, get_user())
    elif request.type == BusinessType.supplier:
        data = business_data_access.create_supplier(request.keyword, "", "", get_user())
    elif request.type == BusinessType.customer:
        data = business_data_access.create_customer(request.keyword, "", "", get_user())
    elif request.type == BusinessType.employee:
        data = business_data_access.create_employee(request.keyword, 0, GenderType.MALE, get_user())
        dep = request.dependencies[0]
        if dep.type == BusinessType.project and data:
            p = business_data_access.get_data_by_cls_id(get_business_db_cls_by_type(dep.type), dep.value, get_user())
            business_data_access.create_employee_project_record(False, p, data)
    else:
        return response(code=ErrorCodes.quick_create_invalid)
    if not data:
        return response(code=ErrorCodes.database_operation_error)
    submit_task(vectorization_pool, vectorize_candidate, get_user().id, data.id, request.type, data.name)
    return response()


add_route("save_internal_transfer_record", save_internal_transfer_record)
add_route("save_transaction_record", save_transaction_record)

add_route("save_employee_salary_bill", save_employee_salary_bill)
add_route("save_employee_loan_bill", save_employee_loan_bill)
add_route("save_receivable_payable_bill", save_receivable_payable_bill)

add_route("save_account_info", save_account_info)
add_route("save_project_info", save_project_info)
add_route("save_employee_info", save_employee_info)
add_route("save_contract_info", save_contract_info)
add_route("save_invoice_info", save_invoice_info)
add_route("save_customer_info", save_customer_info)
add_route("save_supplier_info", save_supplier_info)

add_route("get_combobox_candidate", get_combobox_candidate)
add_route("quick_create_candidate", quick_create_candidate)
