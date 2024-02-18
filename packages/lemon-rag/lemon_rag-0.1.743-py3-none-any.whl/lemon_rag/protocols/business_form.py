from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from lemon_rag.api.local import get_user
from lemon_rag.dependencies.data_access import business_data_access
from lemon_rag.protocols.business_enum import TransactionType, ReceivablePayableType, TransactionItem, ContractType, \
    InvoiceType, GenderType
from lemon_rag.protocols.chat import FormSchema, FormFieldSchema, FormControlComponent, InputSettings, SelectSettings, \
    MoneySettings, NumberSettings, DatetimeSettings, OptionPair, BusinessDataType, BusinessType, OptionsParam, \
    DatetimeFieldSchema, InputFieldSchema, SelectFieldSchema, MoneyFieldSchema, NumberFieldSchema, \
    ConditionalFieldSchema, ConditionalSettings, ConditionalField, VisibleCondition, Dependency, DependencyType


class FieldMapping(BaseModel):
    name: str
    label: str
    required: bool = True
    editable: bool = True


def get_form_transaction_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        DatetimeFieldSchema(
            db_field_name="date", name="date", label="日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="voucher_number", name="voucher_number", label="凭证号", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        SelectFieldSchema(
            db_field_name="type", name="type", label="类型",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(
                options=[OptionPair(label=item, value=item) for item in TransactionType.__members__.values()])
        ),
        SelectFieldSchema(
            db_field_name="account", name="account_name", label="账户",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.account))
        ),
        SelectFieldSchema(
            db_field_name="transaction_item", name="usage", label="收支项目",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.transaction_item))
        ),
        InputFieldSchema(
            db_field_name="description", name="summary", label="业务摘要",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        MoneyFieldSchema(
            db_field_name="amount", name="amount", label="金额",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        SelectFieldSchema(
            db_field_name="project", name="project_name", label="项目名称", required=False,
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.project))
        ),
        # SelectFieldSchema(
        #     db_field_name="contract", name="contract_number", label="合同号", required=False,
        #     control_component=FormControlComponent.SELECT,
        #     field_settings=SelectSettings(options_params=OptionsParam(
        #         type=BusinessType.contract, dependencies=[Dependency(name="project_name", type=BusinessType.project)]))
        # ),
        ConditionalFieldSchema(
            db_field_name="related_description", name="related_receivable_or_payable_bill", label="关联业务摘要",
            control_component=FormControlComponent.CONDITION,
            field_settings=ConditionalSettings(
                fields=[
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="usage", target_value=
                        str(business_data_access.get_transaction_item_by_name(
                            TransactionItem.RECEIVABLE.value, get_user()).id))],
                        fields=[SelectFieldSchema(
                            db_field_name="receivable_description", name="receivable_description", label="应收摘要",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(
                                options_params=OptionsParam(
                                    type=BusinessType.receivable_payable,
                                    dependencies=[
                                        Dependency(name="project_name", type=BusinessType.project),
                                        Dependency(name="type", value=ReceivablePayableType.RECEIVABLE,
                                                   dependency_type=DependencyType.CONST)
                                    ]
                                )
                            )
                        )]
                    ),
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="usage", target_value=
                        str(business_data_access.get_transaction_item_by_name(
                            TransactionItem.PAYABLE.value, get_user()).id))],
                        fields=[SelectFieldSchema(
                            db_field_name="payable_description", name="payable_description", label="应付摘要",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(
                                options_params=OptionsParam(
                                    type=BusinessType.receivable_payable,
                                    dependencies=[
                                        Dependency(name="project_name", type=BusinessType.project),
                                        Dependency(name="type", value=ReceivablePayableType.PAYABLE,
                                                   dependency_type=DependencyType.CONST)
                                    ]
                                )
                            )
                        )]
                    ),
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="usage", target_value=
                        str(business_data_access.get_transaction_item_by_name(
                            TransactionItem.LOAN.value, get_user()).id))],
                        fields=[SelectFieldSchema(
                            db_field_name="advancing_description", name="advancing_description", label="员工借款",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.employee_loan)))
                        ]
                    ),
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="usage", target_value=
                        str(business_data_access.get_transaction_item_by_name(
                            TransactionItem.REPAYMENT.value, get_user()).id))],
                        fields=[SelectFieldSchema(
                            db_field_name="repayment_description", name="repayment_description", label="还款摘要",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.employee_loan)))
                        ]
                    ),
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="usage", target_value=
                        str(business_data_access.get_transaction_item_by_name(
                            TransactionItem.SALARY.value, get_user()).id))],
                        fields=[SelectFieldSchema(
                            db_field_name="salary_description", name="salary_description", label="工资摘要",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.salary)))]
                    ),
                ]
            )
        ),
        InputFieldSchema(
            db_field_name="notes", name="notes", label="备注", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.transaction)


def get_form_internal_transfer_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        DatetimeFieldSchema(
            db_field_name="date", name="date", label="日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="description", name="service_description", label="业务描述",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        SelectFieldSchema(
            db_field_name="source_account", name="source_account_name", label="转出账户",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.account))
        ),
        SelectFieldSchema(
            db_field_name="target_account", name="target_account_name", label="转入账户",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.account))
        ),
        MoneyFieldSchema(
            db_field_name="amount", name="amount", label="金额", editable=False,
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.internal_transfer)


def get_form_receivable_payable_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        DatetimeFieldSchema(
            db_field_name="date", name="date", label="日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="description", name="summary", label="摘要",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        SelectFieldSchema(
            db_field_name="type", name="type", label="类型",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(
                options=[OptionPair(label=item, value=item) for item in ReceivablePayableType.__members__.values()])
        ),
        SelectFieldSchema(
            db_field_name="project", name="project_name", label="项目名称",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.project))
        ),
        SelectFieldSchema(
            db_field_name="employee", name="handler_name", label="经办人",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(
                type=BusinessType.employee, dependencies=[Dependency(name="project_name", type=BusinessType.project)]))
        ),
        SelectFieldSchema(
            db_field_name="contract", name="contract_number", label="合同号", required=False,
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(
                type=BusinessType.contract, dependencies=[Dependency(name="project_name", type=BusinessType.project)]))
        ),
        InputFieldSchema(
            db_field_name="product_name", name="product_name", label="商品名称", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        InputFieldSchema(
            db_field_name="specification", name="product_specification", label="规格型号", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        NumberFieldSchema(
            db_field_name="quantity", name="quantity", label="数量",
            control_component=FormControlComponent.NUMBER,
            field_settings=NumberSettings()
        ),
        MoneyFieldSchema(
            db_field_name="unit_price", name="unit_price", label="单价",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        InputFieldSchema(
            db_field_name="notes", name="notes", label="备注", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="start_date", name="start_date", label="开始时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="end_date", name="end_date", label="结束时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
    ]
    return FormSchema(fields=fields, type=BusinessDataType.receivable_payable)


def get_form_employee_loan_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        DatetimeFieldSchema(
            db_field_name="date", name="date", label="日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="description", name="summary", label="摘要",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        SelectFieldSchema(
            db_field_name="employee", name="employee", label="借款人",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.employee))
        ),
        MoneyFieldSchema(
            db_field_name="amount", name="amount", label="金额",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        MoneyFieldSchema(
            db_field_name="adjustment_amount", name="adjustment_amount", label="调整金额", required=False,
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        DatetimeFieldSchema(
            db_field_name="start_date", name="apply_date", label="开始时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="end_date", name="due_date", label="结束时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.employee_loan)


def get_form_employee_salary_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        SelectFieldSchema(
            db_field_name="employee", name="employee_name", label="员工名称",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.employee))
        ),
        NumberFieldSchema(
            db_field_name="attendance_days", name="days_attended", label="出勤天数",
            control_component=FormControlComponent.NUMBER,
            field_settings=NumberSettings()
        ),
        MoneyFieldSchema(
            db_field_name="basic_salary", name="total_basic_salary", label="基础工资",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        MoneyFieldSchema(
            db_field_name="bonus", name="bonus", label="奖金",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        MoneyFieldSchema(
            db_field_name="other_deductions", name="other_deductions", label="其他扣款",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        DatetimeFieldSchema(
            db_field_name="start_date", name="work_start_date", label="开始日期",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="end_date", name="work_end_date", label="结束日期",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="date", name="expected_pay_date", label="支付日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="description", name="service_description", label="摘要",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        # MoneyFieldSchema(
        #     db_field_name="overtime_pay", name="overtime_pay", label="加班费",
        #     control_component=FormControlComponent.MONEY,
        #     field_settings=MoneySettings()
        # ),
        # MoneyFieldSchema(
        #     db_field_name="attendance_bonus", name="attendance_bonus", label="全勤奖",
        #     control_component=FormControlComponent.MONEY,
        #     field_settings=MoneySettings()
        # ),
        # MoneyFieldSchema(
        #     db_field_name="subsidy", name="subsidy", label="补贴",
        #     control_component=FormControlComponent.MONEY,
        #     field_settings=MoneySettings()
        # ),

        # MoneyFieldSchema(
        #     db_field_name="leave_deduction", name="leave_deduction", label="请假扣款",
        #     control_component=FormControlComponent.MONEY,
        #     field_settings=MoneySettings()
        # ),

    ]
    return FormSchema(fields=fields, type=BusinessDataType.employee_salary)


def get_form_contract_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        DatetimeFieldSchema(
            db_field_name="date", name="date", label="日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="number", name="contract_number", label="合同号",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        InputFieldSchema(
            db_field_name="name", name="contract_name", label="合同名称",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        SelectFieldSchema(
            db_field_name="project", name="project_name", label="项目名称",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.project))
        ),
        SelectFieldSchema(
            db_field_name="type", name="contract_type", label="合同类型",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(
                options=[OptionPair(label=item, value=item) for item in ContractType.__members__.values()])
        ),
        ConditionalFieldSchema(
            db_field_name="customer_supplier", name="customer_name/supplier_name", label="客商",
            control_component=FormControlComponent.CONDITION,
            field_settings=ConditionalSettings(
                fields=[
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="contract_type", target_value=ContractType.SALES)],
                        fields=[SelectFieldSchema(
                            db_field_name="customer", name="customer_name", label="客户",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.customer)))]
                    ),
                    ConditionalField(
                        conditions=[VisibleCondition(target_key="contract_type", target_value=ContractType.PURCHASE)],
                        fields=[SelectFieldSchema(
                            db_field_name="supplier", name="supplier_name", label="供应商",
                            control_component=FormControlComponent.SELECT,
                            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.supplier)))]
                    )
                ]
            )
        ),
        MoneyFieldSchema(
            db_field_name="amount", name="amount", label="合同金额",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        # MoneyFieldSchema(
        #     db_field_name="adjustment_amount", name="adjustment_amount", label="调整金额", required=False,
        #     control_component=FormControlComponent.MONEY,
        #     field_settings=MoneySettings()
        # ),
        DatetimeFieldSchema(
            db_field_name="start_date", name="start_date", label="开始时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="end_date", name="end_date", label="结束时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="notes", name="notes", label="备注", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.contract)


def get_form_invoice_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        DatetimeFieldSchema(
            db_field_name="date", name="date", label="日期", editable=False,
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        SelectFieldSchema(
            db_field_name="contract", name="contract_number", label="合同号",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.contract))
        ),
        MoneyFieldSchema(
            db_field_name="amount", name="amount", label="含税金额",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        NumberFieldSchema(
            db_field_name="tax_rate", name="tax_rate", label="税率",
            control_component=FormControlComponent.NUMBER,
            field_settings=NumberSettings()
        ),
        SelectFieldSchema(
            db_field_name="type", name="invoice_type", label="发票种类",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(
                options=[OptionPair(label=item, value=item) for item in InvoiceType.__members__.values()])
        ),
        InputFieldSchema(
            db_field_name="number", name="invoice_number", label="发票号码",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        InputFieldSchema(
            db_field_name="code", name="invoice_code", label="发票代码",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        InputFieldSchema(
            db_field_name="content", name="invoice_content", label="发票内容",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="submit_date", name="submit_date", label="交票日期",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        InputFieldSchema(
            db_field_name="notes", name="notes", label="备注", required=False,
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.invoice)


def get_form_employee_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        InputFieldSchema(
            db_field_name="name", name="employee_name", label="员工名称",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        NumberFieldSchema(
            db_field_name="age", name="age", label="年龄",
            control_component=FormControlComponent.NUMBER,
            field_settings=NumberSettings()
        ),
        SelectFieldSchema(
            db_field_name="gender", name="gender", label="性别",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(
                options=[OptionPair(label=item, value=item) for item in GenderType.__members__.values()])
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.employee)


def get_form_project_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        InputFieldSchema(
            db_field_name="name", name="project_name", label="项目名称",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        MoneyFieldSchema(
            db_field_name="budget", name="project_budget", label="项目预算",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        ),
        SelectFieldSchema(
            db_field_name="charger_employee", name="charger_employee", label="负责人",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(options_params=OptionsParam(type=BusinessType.employee))
        ),
        SelectFieldSchema(
            db_field_name="project_members", name="project_members", label="项目成员",
            control_component=FormControlComponent.SELECT,
            field_settings=SelectSettings(multiple=True, options_params=OptionsParam(type=BusinessType.employee))
        ),
        DatetimeFieldSchema(
            db_field_name="start_date", name="start_date", label="开始时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        ),
        DatetimeFieldSchema(
            db_field_name="end_date", name="end_date", label="结束时间",
            control_component=FormControlComponent.DATETIME,
            field_settings=DatetimeSettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.project)


def get_form_account_schema() -> FormSchema:
    fields: List[FormFieldSchema] = [
        InputFieldSchema(
            db_field_name="name", name="account_name", label="账户名称",
            control_component=FormControlComponent.INPUT,
            field_settings=InputSettings()
        ),
        MoneyFieldSchema(
            db_field_name="amount", name="balance", label="账户金额",
            control_component=FormControlComponent.MONEY,
            field_settings=MoneySettings()
        )
    ]
    return FormSchema(fields=fields, type=BusinessDataType.account)


def get_customer_schema() -> FormSchema:
    return FormSchema(
        fields=[
            InputFieldSchema(
                db_field_name="name", name="customer_name", label="客户名称",
                control_component=FormControlComponent.INPUT,
                field_settings=InputSettings()
            ),
            InputFieldSchema(
                db_field_name="contact_name", name="contact_name", label="联系人",
                control_component=FormControlComponent.INPUT,
                field_settings=InputSettings()
            ),
            InputFieldSchema(
                db_field_name="contact_phone", name="contact_mobile_number", label="联系方式",
                control_component=FormControlComponent.INPUT,
                field_settings=InputSettings()
            )
        ],
        type=BusinessDataType.customer
    )


def get_supplier_schema() -> FormSchema:
    return FormSchema(
        fields=[
            InputFieldSchema(
                db_field_name="name", name="supplier_name", label="供应商",
                control_component=FormControlComponent.INPUT,
                field_settings=InputSettings()
            ),
            InputFieldSchema(
                db_field_name="contact_name", name="contact_name", label="联系人",
                control_component=FormControlComponent.INPUT,
                field_settings=InputSettings()
            ),
            InputFieldSchema(
                db_field_name="contact_phone", name="contact_mobile_number", label="联系方式",
                control_component=FormControlComponent.INPUT,
                field_settings=InputSettings()
            )
        ],
        type=BusinessDataType.supplier
    )


def get_form_schema_by_type(data_type: BusinessDataType) -> Optional[FormSchema]:
    if data_type == BusinessDataType.transaction:
        return get_form_transaction_schema()
    if data_type == BusinessDataType.internal_transfer:
        return get_form_internal_transfer_schema()  #
    if data_type == BusinessDataType.receivable_payable:
        return get_form_receivable_payable_schema()  #
    if data_type == BusinessDataType.employee_loan:
        return get_form_employee_loan_schema()  #
    if data_type == BusinessDataType.employee_salary:
        return get_form_employee_salary_schema()  #
    if data_type == BusinessDataType.contract:
        return get_form_contract_schema()  #
    if data_type == BusinessDataType.invoice:
        return get_form_invoice_schema()  #
    if data_type == BusinessDataType.employee:
        return get_form_employee_schema()  #
    if data_type == BusinessDataType.project:
        return get_form_project_schema()  #
    if data_type == BusinessDataType.account:
        return get_form_account_schema()  #
    if data_type == BusinessDataType.customer:
        return get_customer_schema()
    if data_type == BusinessDataType.supplier:
        return get_supplier_schema()
    return None


if __name__ == '__main__':
    print(get_form_employee_schema().json())
