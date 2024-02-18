import decimal
from typing import List, Dict, Type, Tuple, Union

import peewee
from pydantic import ValidationError, BaseModel
from pydantic.error_wrappers import ErrorWrapper

from lemon_rag.dependencies.data_access import business_data_access
from lemon_rag.lemon_runtime import models
from lemon_rag.protocols.business import ProjectInfo, InternalTransferRecord, ContractInfo, InvoiceInfo, SalaryBill, \
    PaymentAccount, EmployeeInfo, LoanBill, ReceivablePayableBill, CustomerInfo, SupplierInfo, SalesContract, \
    PurchaseContract, TransactionRecord
from lemon_rag.protocols.business_enum import TransactionType, TransactionItem
from lemon_rag.protocols.business_form import get_form_schema_by_type
from lemon_rag.protocols.chat import BusinessType, FormValidationError, Form
from lemon_rag.utils import log
from lemon_rag.utils.api_utils import get_business_db_cls_by_type


def raise_validation_error(msg: str, filed_name: str, cls_for_field: Type[BaseModel]):
    error = ErrorWrapper(exc=ValueError(msg), loc=(filed_name,))
    raise ValidationError(errors=[error], model=cls_for_field)


def check_field_existence(
        id_: str, filed_name: str, type_: BusinessType, cls_for_field: Type[BaseModel], msg: str,
        creator: models.AuthUserTab
) -> peewee.Model:
    if not id_:
        raise_validation_error(msg, filed_name, cls_for_field)
    data = business_data_access.get_data_by_cls_id(get_business_db_cls_by_type(type_), int(id_), creator)
    if not data:
        raise_validation_error(msg, filed_name, cls_for_field)
    return data


def account_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        account_value_map = form_schema.to_db_value_map(form.data)
        try:
            account_info = PaymentAccount(**account_value_map)
            if business_data_access.get_account_by_name(account_info.name, creator):
                raise_validation_error("账户已存在", "name", PaymentAccount)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def account_save_event(account_info: PaymentAccount, creator: models.AuthUserTab) -> models.AccountTab:
    account = business_data_access.create_account(account_info.name, account_info.amount, creator)
    return account


def employee_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        employee_value_map = form_schema.to_db_value_map(form.data)
        try:
            employee_info = EmployeeInfo(**employee_value_map)
            if business_data_access.get_employee_by_name(employee_info.name, creator):
                raise_validation_error("员工已存在", "name", EmployeeInfo)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def employee_save_event(employee_info: EmployeeInfo, creator: models.AuthUserTab) -> models.EmployeeTab:
    employee = business_data_access.create_employee(
        employee_info.name, employee_info.age, employee_info.gender, creator)
    return employee


def project_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        project_value_map = form_schema.to_db_value_map(form.data)
        try:
            project_info = ProjectInfo(**project_value_map)
            if business_data_access.get_project_by_name(project_info.name, creator):
                raise_validation_error("项目已存在", "name", ProjectInfo)
            project_members = project_info.project_members.split(",")
            if project_info.charger_employee not in project_members:
                project_members.append(project_info.charger_employee)
            for member in project_members:
                check_field_existence(
                    member, "charger_employee" if member == project_info.charger_employee else "project_members",
                    BusinessType.employee, ProjectInfo, "包含不存在员工", creator)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def project_save_event(project_info: ProjectInfo, creator: models.AuthUserTab) -> models.ProjectTab:
    project = business_data_access.create_project(
        project_info.name, project_info.start_date, project_info.end_date, project_info.budget, creator)
    project_members = project_info.project_members.split(",")
    if project_info.charger_employee not in project_members:
        project_members.append(project_info.charger_employee)
    for member in project_members:
        employee = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.employee), int(member), creator)
        business_data_access.create_employee_project_record(
            bool(member == project_info.charger_employee), project, employee)
    return project


def internal_transfer_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    accounts: Dict[str, decimal.Decimal] = {}
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        internal_transfer_value_map = form_schema.to_db_value_map(form.data)
        try:
            internal_transfer = InternalTransferRecord(**internal_transfer_value_map)
            # 验证账户是否存在
            source_account = check_field_existence(
                internal_transfer.source_account, "source_account",
                BusinessType.account, InternalTransferRecord, "转出账户不存在", creator)
            accounts[str(source_account.id)] = accounts.get(str(source_account.id), source_account.amount)
            target_account = check_field_existence(
                internal_transfer.target_account, "target_account",
                BusinessType.account, InternalTransferRecord, "转入账户不存在", creator)
            accounts[str(target_account.id)] = accounts.get(str(target_account.id), target_account.amount)

            # 验证账户是否能够转账
            if accounts.get(str(target_account.id)) < internal_transfer.amount:
                error = ErrorWrapper(
                    exc=ValueError(
                        f"{source_account.name}余额为：{round(accounts.get(str(source_account.id)), 2)}, 不足以转账"),
                    loc=('amount',))
                raise ValidationError(errors=[error], model=InternalTransferRecord)
            accounts[str(source_account.id)] = accounts.get(str(source_account.id)) - internal_transfer.amount
            accounts[str(target_account.id)] = accounts.get(str(target_account.id)) + internal_transfer.amount
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def internal_transfer_save_event(
        record: InternalTransferRecord, creator: models.AuthUserTab) -> models.InternalTransferTab:
    source_account = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.account), int(record.source_account), creator)
    target_account = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.account), int(record.target_account), creator)
    internal_transfer = business_data_access.create_internal_transfer_record(
        source_account, target_account, record.amount, record.description, record.date, creator)
    business_data_access.update_account_amount_by_id(source_account.id, source_account.amount - record.amount, creator)
    business_data_access.update_account_amount_by_id(target_account.id, target_account.amount + record.amount, creator)
    return internal_transfer


def contract_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        contract_value_map = form_schema.to_db_value_map(form.data)
        try:
            contract_info = ContractInfo.create_contract(contract_value_map)
            if business_data_access.get_contract_by_number_name(contract_info.number, contract_info.name, creator):
                raise_validation_error("合同已存在", "number", ContractInfo)
            # 验证项目是否存在
            check_field_existence(
                contract_info.project, "project", BusinessType.project, ContractInfo, "项目不存在", creator)
            # 验证供应商或客户是否存在
            if isinstance(contract_info, SalesContract):
                check_field_existence(
                    contract_info.customer, "customer", BusinessType.customer, ContractInfo, "客户不存在", creator)
            if isinstance(contract_info, PurchaseContract):
                check_field_existence(
                    contract_info.supplier, "supplier", BusinessType.supplier, ContractInfo, "供应商不存在", creator)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def contract_save_event(
        contract_info: Union['SalesContract', 'PurchaseContract'], creator: models.AuthUserTab
) -> models.ContractTab:
    customer, supplier = None, None
    project = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.project), int(contract_info.project), creator)
    if isinstance(contract_info, SalesContract):
        customer = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.customer), int(contract_info.customer), creator)
    if isinstance(contract_info, PurchaseContract):
        supplier = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.supplier), int(contract_info.supplier), creator)
    contract = business_data_access.create_contract(contract_info, project, customer, supplier, creator)
    return contract


def invoice_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    # allow invoicing amount
    invoice_amount: Dict[str, decimal.Decimal] = {}
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        invoice_value_map = form_schema.to_db_value_map(form.data)
        try:
            invoice = InvoiceInfo(**invoice_value_map)
            if business_data_access.get_invoice_by_number_code(invoice.number, invoice.code, creator):
                raise_validation_error("发票已存在", "number", InvoiceInfo)
            # 验证合同是否存在
            contract = check_field_existence(
                invoice.contract, "contract", BusinessType.contract, InvoiceInfo, "合同不存在", creator)
            invoice_amount[str(contract.id)] = invoice_amount.get(str(contract.id), contract.completed_amount)
            # 合同完成金额可开发票，发票金额不能超过合同完成金额
            if invoice_amount.get(str(contract.id)) < invoice.amount:
                error = ErrorWrapper(
                    exc=ValueError(f"发票{invoice.number}的金额超过合同完成金额，不能录入该发票"), loc=('amount',))
                raise ValidationError(errors=[error], model=InternalTransferRecord)
            invoice_amount[str(contract.id)] = invoice_amount.get(str(contract.id)) - invoice.amount
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def invoice_save_event(invoice_info: InvoiceInfo, creator: models.AuthUserTab) -> models.InvoiceTab:
    contract = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.contract), int(invoice_info.contract), creator)
    invoice = business_data_access.create_invoice(invoice_info, contract, creator)
    invoice_total_amount = contract.invoice_total_amount + invoice.amount
    business_data_access.update_contract_invoice_amount_by_id(contract.id, invoice_total_amount, creator)
    return invoice


def customer_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        customer_value_map = form_schema.to_db_value_map(form.data)
        try:
            customer_info = CustomerInfo(**customer_value_map)
            if business_data_access.get_customer_by_name(customer_info.name, creator):
                raise_validation_error("客户已存在", "name", CustomerInfo)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def customer_save_event(customer_info: CustomerInfo, creator: models.AuthUserTab) -> models.CustomerTab:
    customer = business_data_access.create_customer(
        customer_info.name, customer_info.contact_name, customer_info.contact_phone, creator)
    return customer


def supplier_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        supplier_value_map = form_schema.to_db_value_map(form.data)
        try:
            supplier_info = SupplierInfo(**supplier_value_map)
            if business_data_access.get_supplier_by_name(supplier_info.name, creator):
                raise_validation_error("供应商已存在", "name", SupplierInfo)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def supplier_save_event(supplier_info: SupplierInfo, creator: models.AuthUserTab) -> models.SupplierTab:
    supplier = business_data_access.create_supplier(
        supplier_info.name, supplier_info.contact_name, supplier_info.contact_phone, creator)
    return supplier


def salary_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        salary_value_map = form_schema.to_db_value_map(form.data)
        try:
            salary_info = SalaryBill(**salary_value_map)
            # 验证员工是否存在
            check_field_existence(
                salary_info.employee, "employee", BusinessType.employee, SalaryBill, "员工不存在", creator)
            # if business_data_access.get_salary_by_date_name(salary_info.date, employee, creator):
            #     raise_validation_error("员工当月工资条已存在", "employee", SalaryBill)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def salary_save_event(salary_bill: SalaryBill, creator: models.AuthUserTab) -> models.SalaryTab:
    employee = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.employee), int(salary_bill.employee), creator)
    # if business_data_access.get_salary_by_description(salary_bill.description, get_user()):
    #     salary_bill.description = f"{employee.name}在{salary_bill.start_date}至{salary_bill.end_date}的工资单"
    salary = business_data_access.create_employee_salary(salary_bill, employee, creator)
    log.info(f"创建了一个工资单{salary}")
    return salary


def employee_loan_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        loan_value_map = form_schema.to_db_value_map(form.data)
        try:
            loan_bill = LoanBill(**loan_value_map)
            # 验证员工是否存在
            check_field_existence(
                loan_bill.employee, "employee", BusinessType.employee, LoanBill, "员工不存在", creator)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def employee_loan_save_event(loan_bill: LoanBill, creator: models.AuthUserTab) -> Tuple[models.EmployeeLoanTab, bool]:
    employee = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.employee), int(loan_bill.employee), creator)
    old_loan_bill = business_data_access.get_employ_loan_by_date_name_description(
        loan_bill.date, employee, loan_bill.description, creator)
    if old_loan_bill:
        adjustment_amount = old_loan_bill.adjustment_amount + loan_bill.amount + loan_bill.adjustment_amount
        business_data_access.update_loan_adjust_amount_by_date_name_description(
            adjustment_amount, loan_bill.date, employee, loan_bill.description, creator)
        updated_loan_bill = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.employee_loan), old_loan_bill.id, creator)
        return updated_loan_bill, False
    # if business_data_access.get_employee_loan_by_description(loan_bill.description, creator):
    #     loan_bill.description = f"{employee.name}在{loan_bill.date}借了{loan_bill.amount + loan_bill.adjustment_amount}元"
    employee_loan = business_data_access.create_employee_loan(loan_bill, employee, creator)
    return employee_loan, True


def receivable_payable_save_before_validate(
        forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        receivable_payable_value_map = form_schema.to_db_value_map(form.data)
        try:
            rp_bill = ReceivablePayableBill(**receivable_payable_value_map)
            # 验证项目是否存在
            check_field_existence(
                rp_bill.project, "project", BusinessType.project, LoanBill, "项目不存在", creator)
            # 验证经办人是否存在
            check_field_existence(
                rp_bill.employee, "employee", BusinessType.employee, LoanBill, "经办人不存在", creator)
        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def receivable_payable_save_event(
        receivable_payable_bill: ReceivablePayableBill, creator: models.AuthUserTab) -> models.ReceivablePayableTab:
    project = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.project), int(receivable_payable_bill.project), creator)
    employee = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.employee), int(receivable_payable_bill.employee), creator)
    if receivable_payable_bill.contract:
        contract = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.contract), int(receivable_payable_bill.contract), creator)
    else:
        contract = None
    rp = business_data_access.create_receivable_payable(receivable_payable_bill, project, employee, contract, creator)
    return rp


def transaction_save_before_validate(forms: List[Form], creator: models.AuthUserTab) -> List[FormValidationError]:
    errors: List[FormValidationError] = []
    accounts: Dict[str, decimal.Decimal] = {}
    receivable_remain_amount: Dict[str, decimal.Decimal] = {}
    payable_remain_amount: Dict[str, decimal.Decimal] = {}
    repayment_remain_amount: Dict[str, decimal.Decimal] = {}
    loan_remain_amount: Dict[str, decimal.Decimal] = {}
    salary_remain_amount: Dict[str, decimal.Decimal] = {}
    for form in forms:
        form_schema = get_form_schema_by_type(form.type)
        transaction_value_map = form_schema.to_db_value_map(form.data)
        try:
            t_record = TransactionRecord(**transaction_value_map)
            # 验证账户是否存在
            account = check_field_existence(
                t_record.account, "account", BusinessType.account, TransactionRecord, "账户不存在", creator)
            accounts[str(account.id)] = accounts.get(str(account.id), account.amount)
            # 验证收支项目是否存在
            transaction_item = check_field_existence(
                t_record.transaction_item, "transaction_item", BusinessType.transaction_item,
                TransactionRecord, "收支项目不存在", creator)
            # 验证项目是否存在
            check_field_existence(
                t_record.project, "project", BusinessType.project, TransactionRecord,
                "项目不存在", creator)
            # 验证钱是否够扣除
            if t_record.type == TransactionType.INCOME:
                accounts[str(account.id)] = accounts.get(str(account.id)) + t_record.amount
            if t_record.type == TransactionType.EXPENSE:
                if accounts.get(str(account.id)) < t_record.amount:
                    msg = f"账户余额为：{round(accounts.get(str(account.id)), 2)}，不足以支付"
                    raise_validation_error(msg, "account", TransactionRecord)
                accounts[str(account.id)] = accounts.get(str(account.id)) - t_record.amount

            # 应收一定要有应收摘要
            if transaction_item.name == TransactionItem.RECEIVABLE:
                receivable_bill = check_field_existence(
                    t_record.receivable_description, "receivable_description", BusinessType.receivable_payable,
                    TransactionRecord, "应收单不存在", creator)
                # 交易金额不能超过剩余应收
                receivable_remain_amount[str(receivable_bill.id)] = (
                    receivable_remain_amount.get(str(receivable_bill.id),
                                                 receivable_bill.amount - receivable_bill.completed_amount))
                if receivable_remain_amount.get(str(receivable_bill.id)) < t_record.amount:
                    msg = f"交易金额超过完成应收({round(receivable_remain_amount.get(str(receivable_bill.id)), 2)}元)"
                    raise_validation_error(msg, "amount", TransactionRecord)
                receivable_remain_amount[str(receivable_bill.id)] = receivable_remain_amount.get(
                    str(receivable_bill.id)) - t_record.amount

            # 应付一定要有应付摘要
            if transaction_item.name == TransactionItem.PAYABLE:
                payable_bill = check_field_existence(
                    t_record.payable_description, "payable_description", BusinessType.receivable_payable,
                    TransactionRecord, "应付单不存在", creator)
                # 交易金额不能超过剩余应付
                payable_remain_amount[str(payable_bill.id)] = (
                    payable_remain_amount.get(str(payable_bill.id),
                                              payable_bill.amount - payable_bill.completed_amount))
                if payable_remain_amount.get(str(payable_bill.id)) < t_record.amount:
                    msg = f"交易金额超过剩余应付({round(payable_remain_amount.get(str(payable_bill.id)), 2)}元)"
                    raise_validation_error(msg, "amount", TransactionRecord)
                payable_remain_amount[str(payable_bill.id)] = payable_remain_amount.get(
                    str(payable_bill.id)) - t_record.amount

            # 员工借款一定要有借款摘要
            if transaction_item.name == TransactionItem.LOAN:
                loan_bill = check_field_existence(
                    t_record.advancing_description, "advancing_description", BusinessType.employee_loan,
                    TransactionRecord, "借款单不存在", creator)
                # 交易金额不能超过剩余借款
                loan_remain_amount[str(loan_bill.id)] = (
                    loan_remain_amount.get(str(loan_bill.id),
                                           loan_bill.amount + loan_bill.adjustment_amount - loan_bill.completed_amount))
                if loan_remain_amount.get(str(loan_bill.id)) < t_record.amount:
                    msg = f"交易金额超过剩余借款({round(loan_remain_amount.get(str(loan_bill.id)), 2)}元)"
                    raise_validation_error(msg, "amount", TransactionRecord)
                loan_remain_amount[str(loan_bill.id)] = loan_remain_amount.get(str(loan_bill.id)) - t_record.amount

            # 员工还款一定要有还款摘要
            if transaction_item.name == TransactionItem.REPAYMENT:
                repayment_bill = check_field_existence(
                    t_record.repayment_description, "repayment_description", BusinessType.employee_loan,
                    TransactionRecord, "还款单不存在", creator)
                # 交易金额不能超过剩余还款
                repayment_remain_amount[str(repayment_bill.id)] = (
                    repayment_remain_amount.get(
                        str(repayment_bill.id),
                        repayment_bill.amount + repayment_bill.adjustment_amount - repayment_bill.repayment_amount))
                if repayment_remain_amount.get(str(repayment_bill.id)) < t_record.amount:
                    msg = f"交易金额超过剩余还款({round(repayment_remain_amount.get(str(repayment_bill.id)), 2)}元)"
                    raise_validation_error(msg, "amount", TransactionRecord)
                repayment_remain_amount[str(repayment_bill.id)] = repayment_remain_amount.get(
                    str(repayment_bill.id)) - t_record.amount

            # 员工工资一定要有工资摘要
            if transaction_item.name == TransactionItem.SALARY:
                salary_bill = check_field_existence(
                    t_record.salary_description, "salary_description", BusinessType.salary,
                    TransactionRecord, "工资单不存在", creator)
                # 交易金额不能超过剩余支付工资
                salary_remain_amount[str(salary_bill.id)] = (
                    salary_remain_amount.get(str(salary_bill.id), salary_bill.net_salary - salary_bill.completed_amount))
                if salary_remain_amount.get(str(salary_bill.id)) < t_record.amount:
                    msg = f"交易金额超过剩余支付工资({round(salary_remain_amount.get(str(salary_bill.id)), 2)}元)"
                    raise_validation_error(msg, "amount", TransactionRecord)
                salary_remain_amount[str(salary_bill.id)] = salary_remain_amount.get(
                    str(salary_bill.id)) - t_record.amount

        except ValidationError as e:
            errors.extend([FormValidationError(
                form_id=form.id, error=err.get("msg"), name=form_schema.get_name_by_db_field_name(name))
                for err in e.errors() for name in err.get("loc", [])])
    return errors


def transaction_save_event(t_record: TransactionRecord, creator: models.AuthUserTab) -> models.TransactionTab:
    old_a = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.account), int(t_record.account), creator)
    if t_record.type == TransactionType.INCOME:
        business_data_access.update_account_amount_by_id(int(t_record.account), old_a.amount + t_record.amount, creator)
    if t_record.type == TransactionType.EXPENSE:
        business_data_access.update_account_amount_by_id(int(t_record.account), old_a.amount - t_record.amount, creator)

    new_a = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.account), int(t_record.account), creator)
    transaction_item = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.transaction_item), int(t_record.transaction_item), creator)
    project = business_data_access.get_data_by_cls_id(
        get_business_db_cls_by_type(BusinessType.project), int(t_record.project), creator)

    receivable_payable_bill, loan_repayment_bill, salary_bill = None, None, None

    if transaction_item.name in [TransactionItem.RECEIVABLE, TransactionItem.PAYABLE]:
        if transaction_item.name == TransactionItem.RECEIVABLE:
            receivable_payable_id = t_record.receivable_description
        else:
            receivable_payable_id = t_record.payable_description
        receivable_payable_bill = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.receivable_payable), int(receivable_payable_id), creator)
        # 更新应收应付
        rp_completed_amount = receivable_payable_bill.completed_amount + t_record.amount
        write_off = bool(rp_completed_amount >= receivable_payable_bill.amount)
        business_data_access.update_receivable_payable_completed_amount_write_off_by_id(
            receivable_payable_bill.id, rp_completed_amount, write_off, creator)

        # 更新合同
        if receivable_payable_bill.contract:
            c_completed_amount = receivable_payable_bill.contract.completed_amount + t_record.amount
            c_schedule = c_completed_amount / receivable_payable_bill.contract.total_amount
            business_data_access.update_contract_completed_amount_schedule_by_id(
                receivable_payable_bill.contract.id, c_completed_amount, c_schedule, creator)

    elif transaction_item.name == TransactionItem.LOAN:
        loan_repayment_bill = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.employee_loan), int(t_record.advancing_description), creator)
        # 更新借款
        l_completed_amount = loan_repayment_bill.completed_amount + t_record.amount
        business_data_access.update_employee_loan_completed_amount_by_id(
            loan_repayment_bill.id, l_completed_amount, creator)

    elif transaction_item.name == TransactionItem.REPAYMENT:
        loan_repayment_bill = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.employee_loan), int(t_record.repayment_description), creator)
        # 更新还款
        repayment_amount = loan_repayment_bill.repayment_amount + t_record.amount
        write_off = bool(
            (repayment_amount + loan_repayment_bill.offset_count) >= loan_repayment_bill.completed_amount)
        business_data_access.update_employee_repayment_amount_write_off_by_id(
            loan_repayment_bill.id, repayment_amount, write_off, creator)

    elif transaction_item.name == TransactionItem.SALARY:
        salary_bill = business_data_access.get_data_by_cls_id(
            get_business_db_cls_by_type(BusinessType.salary), int(t_record.salary_description), creator)
        # 更新员工工资
        s_completed_amount = salary_bill.completed_amount + t_record.amount
        write_off = bool(s_completed_amount >= salary_bill.net_salary)
        business_data_access.update_salary_completed_amount_write_off_by_id(
            salary_bill.id, s_completed_amount, write_off, creator)
    transaction = business_data_access.create_transaction(
        t_record, new_a, transaction_item, project, receivable_payable_bill, salary_bill, loan_repayment_bill, creator)
    return transaction
