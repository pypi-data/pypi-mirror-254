import decimal
from datetime import datetime
from typing import Optional, Dict, Union

from pydantic import BaseModel, Field, validator

from lemon_rag.protocols.business_enum import TransactionType, ContractType, GenderType, InvoiceType, \
    ReceivablePayableType


class StartEndDateValidator(BaseModel):
    start_date: str
    end_date: str

    @validator("start_date", always=True)
    def check_start_date(cls, start_date: str):
        start_date = datetime.strptime(start_date, '%Y年%m月%d日')
        return start_date.strftime('%Y年%m月%d日')

    @validator("end_date", always=True)
    def check_end_date(cls, end_date: str, values: dict):
        end_date = datetime.strptime(end_date, '%Y年%m月%d日').strftime('%Y年%m月%d日')
        if 'start_date' in values and end_date < values['start_date']:
            raise ValueError("结束时间必须在开始时间之后")
        return end_date


class DateValidator(BaseModel):
    date: str

    @validator("date", always=True)
    def check_date(cls, date: str):
        date = datetime.strptime(date, '%Y年%m月%d日')
        return date.strftime('%Y年%m月%d日')


class PaymentAccount(BaseModel):
    name: str
    amount: decimal.Decimal = Field(gt=0)


class EmployeeInfo(BaseModel):
    name: str = Field(min_length=2, max_length=16)
    age: int = Field(ge=0, le=200)
    gender: GenderType


class ProjectInfo(StartEndDateValidator):
    name: str = Field(min_length=2, max_length=30)
    budget: decimal.Decimal = Field(gt=0)
    charger_employee: str = Field(min_length=1, max_length=10)
    project_members: str = Field(min_length=1, max_length=100)


class InternalTransferRecord(DateValidator):
    description: str = Field(min_length=2, max_length=30)
    source_account: str = Field(min_length=1, max_length=10)
    target_account: str = Field(min_length=1, max_length=10)
    amount: decimal.Decimal = Field(gt=0)

    @validator("target_account", always=True)
    def check_account(cls, target_account: str, values: dict):
        if "source_account" in values and values.get("source_account") == target_account:
            raise ValueError("源帐户和目标帐户不能相同")
        return target_account


class TransactionRecord(DateValidator):
    voucher_number: str
    type: TransactionType
    account: str = Field(min_length=1, max_length=10)
    transaction_item: str = Field(min_length=1, max_length=10)
    description: str = Field(min_length=2, max_length=30)
    amount: decimal.Decimal = Field(gt=0)
    project: str = Field(min_length=1, max_length=10)
    receivable_description: Optional[str]
    payable_description: Optional[str]
    advancing_description: Optional[str]
    repayment_description: Optional[str]
    salary_description: Optional[str]
    notes: str


class ContractInfo(DateValidator, StartEndDateValidator):
    number: str = Field(min_length=2, max_length=20)
    name: str = Field(min_length=2, max_length=20)
    type: ContractType
    project: str = Field(min_length=1, max_length=10)
    amount: decimal.Decimal = Field(gt=0)
    adjustment_amount: decimal.Decimal = Field(decimal.Decimal('0'), ge=0)
    notes: str

    @classmethod
    def create_contract(
            cls, contract_value_map: Dict[str, Union[str, int]]) -> Union['SalesContract', 'PurchaseContract']:
        if contract_value_map['type'] == ContractType.SALES:
            return SalesContract(**contract_value_map)
        elif contract_value_map['type'] == ContractType.PURCHASE:
            return PurchaseContract(**contract_value_map)
        else:
            raise ValueError("Invalid contract type")


class SalesContract(ContractInfo):
    type: ContractType = ContractType.SALES
    customer: str


class PurchaseContract(ContractInfo):
    type: ContractType = ContractType.PURCHASE
    supplier: str


class CustomerInfo(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    contact_name: str = Field("")
    contact_phone: str = Field("")


class SupplierInfo(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    contact_name: str = Field("")
    contact_phone: str = Field("")


class InvoiceInfo(DateValidator):
    contract: str = Field(min_length=1, max_length=10)
    amount: decimal.Decimal = Field(gt=0)
    tax_rate: decimal.Decimal = Field(gt=0)
    type: InvoiceType
    number: str = Field(min_length=1, max_length=10)
    code: str = Field(min_length=1, max_length=10)
    content: str = Field(min_length=1, max_length=10)
    submit_date: str
    notes: str

    @validator("submit_date", always=True)
    def check_submit_date(cls, submit_date: str):
        datetime.strptime(submit_date, '%Y年%m月%d日')
        return submit_date


class SalaryBill(DateValidator, StartEndDateValidator):
    description: str = Field(min_length=2, max_length=30)
    employee: str = Field(min_length=1, max_length=10)
    attendance_days: int = Field(gt=0, le=9999)
    basic_salary: decimal.Decimal = Field(gt=0)
    overtime_pay: Optional[decimal.Decimal] = Field(decimal.Decimal("0"), ge=0)
    attendance_bonus: Optional[decimal.Decimal] = Field(decimal.Decimal("0"), ge=0)
    bonus: decimal.Decimal = Field(ge=0)
    subsidy: Optional[decimal.Decimal] = Field(decimal.Decimal("0"), ge=0)

    leave_deduction: Optional[decimal.Decimal] = Field(decimal.Decimal("0"), ge=0)
    other_deductions: decimal.Decimal = Field(ge=0)


class LoanBill(DateValidator, StartEndDateValidator):
    description: str = Field(min_length=2, max_length=30)
    employee: str = Field(min_length=1, max_length=10)
    amount: decimal.Decimal = Field(gt=0)
    adjustment_amount: decimal.Decimal = Field(ge=0)


class ReceivablePayableBill(DateValidator, StartEndDateValidator):
    description: str = Field(min_length=2, max_length=30)
    type: ReceivablePayableType
    project: str = Field(min_length=1, max_length=10)
    employee: str = Field(min_length=1, max_length=10)
    contract: Optional[str]
    product_name: str
    specification: str
    quantity: int = Field(gt=0)
    unit_price: decimal.Decimal = Field(gt=0)
    notes: str
