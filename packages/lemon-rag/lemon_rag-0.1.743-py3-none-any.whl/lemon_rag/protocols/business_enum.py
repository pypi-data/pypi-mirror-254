from enum import Enum


class InvoiceType(str, Enum):
    GENERAL = "普通发票"
    VAT_SPECIAL = "增值税专用发票"


class TransactionType(str, Enum):
    INCOME = "收入"
    EXPENSE = "支出"


class ContractStatus(str, Enum):
    IN_PROGRESS = "执行中"
    EXPIRED = "合同到期"
    EXPIRED_SOON = "即将到期"
    NOT_STARTED = "合同未开始"


class ContractType(str, Enum):
    SALES = "销售合同"
    PURCHASE = "采购合同"


class GenderType(str, Enum):
    MALE = "男"
    FEMALE = "女"


class ReceivablePayableType(str, Enum):
    RECEIVABLE = "应收"
    PAYABLE = "应付"


class TransactionItem(str, Enum):
    RECEIVABLE = "应收收款"
    PAYABLE = "应付付款"
    LOAN = "员工借款"
    REPAYMENT = "员工还款"
    SALARY = "员工工资"
    OTHER_COST = "其他支出"
    OTHER_INCOMING = "其他收入"
