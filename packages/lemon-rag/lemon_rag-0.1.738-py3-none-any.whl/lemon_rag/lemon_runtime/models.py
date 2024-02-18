from datetime import datetime
from decimal import Decimal
from typing import Union, TypeVar, Generic, Iterator, Optional, TypedDict
import peewee

CharField = Union[peewee.CharField, str]
DatetimeField = Union[peewee.DateTimeField, datetime]
TextField = Union[peewee.TextField, str]
IntegerField = Union[peewee.IntegerField, int]
BooleanField = Union[peewee.BooleanField, bool]
FloatField = Union[peewee.FloatField, float]
DoubleField = Union[peewee.DoubleField, float]
DateField = Union[peewee.DateField, str]
DateTimeField = Union[peewee.DateTimeField, str]
TimeField = Union[peewee.TimeField, str]
DecimalField = Union[peewee.DecimalField, Decimal]
PrimaryKeyField = Union[peewee.PrimaryKeyField, int]

T = TypeVar('T')


class ModelSelect(peewee.ModelSelect, Generic[T]):
    def __iter__(self) -> Iterator[T]:
        pass

    def where(self, *expressions) -> 'ModelSelect[T]':
        pass

    def limit(self, value: Optional[int] = None) -> 'ModelSelect[T]':
        pass

    def offset(self, value: Optional[int] = None) -> 'ModelSelect[T]':
        pass


class BackrefAccessor(peewee.BackrefAccessor, Generic[T]):
    pass


class ModelUpdate(peewee.ModelUpdate, Generic[T]):
    def where(self, *expressions) -> 'ModelUpdate[T]':
        pass

    def execute(self, database=None) -> int:
        pass


class BaseModel(peewee.Model):
    id: PrimaryKeyField

class XFConfig(BaseModel):
    app_id: CharField
    api_key: CharField
    api_secret: CharField

    class __InnerFields(TypedDict):
        app_id: str
        api_key: str
        api_secret: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['XFConfig']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['XFConfig']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'XFConfig':
        pass


class OPENAIConfig(BaseModel):
    api_key: CharField
    base_url: CharField

    class __InnerFields(TypedDict):
        api_key: str
        base_url: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['OPENAIConfig']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['OPENAIConfig']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'OPENAIConfig':
        pass


class VectorStoreConfig(BaseModel):
    uri: CharField
    token: CharField

    class __InnerFields(TypedDict):
        uri: str
        token: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['VectorStoreConfig']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['VectorStoreConfig']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'VectorStoreConfig':
        pass


class AuthUserTab(BaseModel):
    username: CharField
    password: CharField
    last_signin: IntegerField
    nickname: CharField
    avatar: CharField
    create_time: IntegerField
    user_quota: Union[BackrefAccessor['UserQuotaTab'], ModelSelect['UserQuotaTab']]
    file: Union[BackrefAccessor['FileUploadRecordTab'], ModelSelect['FileUploadRecordTab']]
    sessions: Union[BackrefAccessor['SessionTab'], ModelSelect['SessionTab']]
    back_sessions: Union[BackrefAccessor['SessionTab'], ModelSelect['SessionTab']]
    messages: Union[BackrefAccessor['MessageTab'], ModelSelect['MessageTab']]
    owned_knowledge_bases: Union[BackrefAccessor['KnowledgeBaseTab'], ModelSelect['KnowledgeBaseTab']]
    tokens: Union[BackrefAccessor['AppAuthTokenTab'], ModelSelect['AppAuthTokenTab']]
    available_knowledge_accesses: Union[BackrefAccessor['KnowledgeBaseAccessTab'], ModelSelect['KnowledgeBaseAccessTab']]
    created_accesses: Union[BackrefAccessor['KnowledgeBaseAccessTab'], ModelSelect['KnowledgeBaseAccessTab']]
    search_history: Union[BackrefAccessor['SearchHistoryTab'], ModelSelect['SearchHistoryTab']]
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]
    account: Union[BackrefAccessor['AccountTab'], ModelSelect['AccountTab']]
    internal_transfer: Union[BackrefAccessor['InternalTransferTab'], ModelSelect['InternalTransferTab']]
    receivable_payable: Union[BackrefAccessor['ReceivablePayableTab'], ModelSelect['ReceivablePayableTab']]
    contract: Union[BackrefAccessor['ContractTab'], ModelSelect['ContractTab']]
    project: Union[BackrefAccessor['ProjectTab'], ModelSelect['ProjectTab']]
    employee: Union[BackrefAccessor['EmployeeTab'], ModelSelect['EmployeeTab']]
    employee_loan: Union[BackrefAccessor['EmployeeLoanTab'], ModelSelect['EmployeeLoanTab']]
    salary: Union[BackrefAccessor['SalaryTab'], ModelSelect['SalaryTab']]
    invoice: Union[BackrefAccessor['InvoiceTab'], ModelSelect['InvoiceTab']]
    customer: Union[BackrefAccessor['CustomerTab'], ModelSelect['CustomerTab']]
    supplier: Union[BackrefAccessor['SupplierTab'], ModelSelect['SupplierTab']]
    transaction_item: Union[BackrefAccessor['TransactionItemTab'], ModelSelect['TransactionItemTab']]
    offset_item: Union[BackrefAccessor['OffsetItemTab'], ModelSelect['OffsetItemTab']]

    class __InnerFields(TypedDict):
        username: str
        password: str
        last_signin: int
        nickname: str
        avatar: str
        create_time: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['AuthUserTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['AuthUserTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'AuthUserTab':
        pass


class UserQuotaTab(BaseModel):
    request_per_min: IntegerField
    request_per_day: IntegerField
    request_per_month: IntegerField
    max_files: IntegerField
    max_single_file_size: IntegerField
    max_total_knowledge_size: IntegerField
    auth_user: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        request_per_min: int
        request_per_day: int
        request_per_month: int
        max_files: int
        max_single_file_size: int
        max_total_knowledge_size: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['UserQuotaTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['UserQuotaTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'UserQuotaTab':
        pass


class KnowledgeBaseFileTab(BaseModel):
    filename: CharField
    extension: CharField
    origin_filename: CharField
    file_size: IntegerField
    total_parts: IntegerField
    vectorized_parts: IntegerField
    content_hash: CharField
    upload_records: Union[BackrefAccessor['FileUploadRecordTab'], ModelSelect['FileUploadRecordTab']]
    paragraph_list: Union[BackrefAccessor['KnowledgeParagraph'], ModelSelect['KnowledgeParagraph']]
    sentences: Union[BackrefAccessor['KnowledgeSentence'], ModelSelect['KnowledgeSentence']]
    knowledgebase_links: Union[BackrefAccessor['KnowledgebaseFileLink'], ModelSelect['KnowledgebaseFileLink']]
    file: Union[BackrefAccessor['FileTab'], ModelSelect['FileTab']]

    class __InnerFields(TypedDict):
        filename: str
        extension: str
        origin_filename: str
        file_size: int
        total_parts: int
        vectorized_parts: int
        content_hash: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['KnowledgeBaseFileTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['KnowledgeBaseFileTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'KnowledgeBaseFileTab':
        pass


class FileUploadRecordTab(BaseModel):
    upload_time: DatetimeField
    first_upload: BooleanField
    file: Union[peewee.ForeignKeyField, 'KnowledgeBaseFileTab']
    uploader: Union[peewee.ForeignKeyField, 'AuthUserTab']
    upload_file: Union[peewee.ForeignKeyField, 'FileTab']

    class __InnerFields(TypedDict):
        upload_time: datetime
        first_upload: bool

    @classmethod
    def select(cls, *fields) -> ModelSelect['FileUploadRecordTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['FileUploadRecordTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'FileUploadRecordTab':
        pass


class SessionTab(BaseModel):
    create_at: IntegerField
    topic: CharField
    last_msg_id: IntegerField
    last_msg_ts: IntegerField
    role: CharField
    title: CharField
    disabled_at: BooleanField
    version: IntegerField
    user: Union[peewee.ForeignKeyField, 'AuthUserTab']
    friend: Union[peewee.ForeignKeyField, 'AuthUserTab']
    messages: Union[BackrefAccessor['MessageTab'], ModelSelect['MessageTab']]
    summarization: Union[BackrefAccessor['MessageSummarizationTab'], ModelSelect['MessageSummarizationTab']]
    sync_history: Union[BackrefAccessor['SyncHistoryTab'], ModelSelect['SyncHistoryTab']]

    class __InnerFields(TypedDict):
        create_at: int
        topic: str
        last_msg_id: int
        last_msg_ts: int
        role: str
        title: str
        disabled_at: bool
        version: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['SessionTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['SessionTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'SessionTab':
        pass


class MessageTab(BaseModel):
    msg_id: IntegerField
    role: CharField
    is_system: BooleanField
    client_ts: IntegerField
    server_ts: IntegerField
    is_answer: BooleanField
    is_system_msg: BooleanField
    support_retry: BooleanField
    support_rating: BooleanField
    content: CharField
    text: CharField
    context_text: CharField
    version: IntegerField
    accepted: BooleanField
    msg_signature: CharField
    rating: IntegerField
    session: Union[peewee.ForeignKeyField, 'SessionTab']
    user: Union[peewee.ForeignKeyField, 'AuthUserTab']
    summarization: Union[peewee.ForeignKeyField, 'MessageSummarizationTab']
    question: Union[peewee.ForeignKeyField, 'MessageTab']
    answers: Union[BackrefAccessor['MessageTab'], ModelSelect['MessageTab']]
    audio: Union[BackrefAccessor['AudioTab'], ModelSelect['AudioTab']]

    class __InnerFields(TypedDict):
        msg_id: int
        role: str
        is_system: bool
        client_ts: int
        server_ts: int
        is_answer: bool
        is_system_msg: bool
        support_retry: bool
        support_rating: bool
        content: str
        text: str
        context_text: str
        version: int
        accepted: bool
        msg_signature: str
        rating: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['MessageTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['MessageTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'MessageTab':
        pass


class KnowledgeBaseTab(BaseModel):
    name: CharField
    max_files: IntegerField
    create_at: IntegerField
    owner: Union[peewee.ForeignKeyField, 'AuthUserTab']
    access_permissions: Union[BackrefAccessor['KnowledgeBaseAccessTab'], ModelSelect['KnowledgeBaseAccessTab']]
    file_links: Union[BackrefAccessor['KnowledgebaseFileLink'], ModelSelect['KnowledgebaseFileLink']]

    class __InnerFields(TypedDict):
        name: str
        max_files: int
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['KnowledgeBaseTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['KnowledgeBaseTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'KnowledgeBaseTab':
        pass


class DevModuleTab(BaseModel):
    name: CharField
    version: CharField
    registry: CharField

    class __InnerFields(TypedDict):
        name: str
        version: str
        registry: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['DevModuleTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['DevModuleTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'DevModuleTab':
        pass


class AppAuthTokenTab(BaseModel):
    create_at: IntegerField
    expire_at: IntegerField
    token: CharField
    comment: CharField
    user: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        create_at: int
        expire_at: int
        token: str
        comment: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['AppAuthTokenTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['AppAuthTokenTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'AppAuthTokenTab':
        pass


class MessageSummarizationTab(BaseModel):
    from_msg_id: IntegerField
    to_msg_id: IntegerField
    summarization: CharField
    msg_count: IntegerField
    session: Union[peewee.ForeignKeyField, 'SessionTab']
    message: Union[BackrefAccessor['MessageTab'], ModelSelect['MessageTab']]

    class __InnerFields(TypedDict):
        from_msg_id: int
        to_msg_id: int
        summarization: str
        msg_count: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['MessageSummarizationTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['MessageSummarizationTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'MessageSummarizationTab':
        pass


class SyncHistoryTab(BaseModel):
    last_read_id: IntegerField
    last_read_ts: IntegerField
    session: Union[peewee.ForeignKeyField, 'SessionTab']

    class __InnerFields(TypedDict):
        last_read_id: int
        last_read_ts: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['SyncHistoryTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['SyncHistoryTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'SyncHistoryTab':
        pass


class KnowledgeBaseAccessTab(BaseModel):
    permission: IntegerField
    create_at: IntegerField
    knowledge_base: Union[peewee.ForeignKeyField, 'KnowledgeBaseTab']
    user: Union[peewee.ForeignKeyField, 'AuthUserTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        permission: int
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['KnowledgeBaseAccessTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['KnowledgeBaseAccessTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'KnowledgeBaseAccessTab':
        pass


class KnowledgeParagraph(BaseModel):
    raw_content: CharField
    index: IntegerField
    context_content: CharField
    total_sentences: IntegerField
    file: Union[peewee.ForeignKeyField, 'KnowledgeBaseFileTab']
    sentences: Union[BackrefAccessor['KnowledgeSentence'], ModelSelect['KnowledgeSentence']]

    class __InnerFields(TypedDict):
        raw_content: str
        index: int
        context_content: str
        total_sentences: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['KnowledgeParagraph']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['KnowledgeParagraph']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'KnowledgeParagraph':
        pass


class KnowledgeSentence(BaseModel):
    index: IntegerField
    raw_content: CharField
    context_content: CharField
    vectorized: BooleanField
    paragraph: Union[peewee.ForeignKeyField, 'KnowledgeParagraph']
    file: Union[peewee.ForeignKeyField, 'KnowledgeBaseFileTab']

    class __InnerFields(TypedDict):
        index: int
        raw_content: str
        context_content: str
        vectorized: bool

    @classmethod
    def select(cls, *fields) -> ModelSelect['KnowledgeSentence']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['KnowledgeSentence']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'KnowledgeSentence':
        pass


class KnowledgebaseFileLink(BaseModel):
    file: Union[peewee.ForeignKeyField, 'KnowledgeBaseFileTab']
    knowledgebase: Union[peewee.ForeignKeyField, 'KnowledgeBaseTab']

    class __InnerFields(TypedDict):
        pass

    @classmethod
    def select(cls, *fields) -> ModelSelect['KnowledgebaseFileLink']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['KnowledgebaseFileLink']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'KnowledgebaseFileLink':
        pass


class FileTab(BaseModel):
    name: CharField
    path: CharField
    type: CharField
    extension: CharField
    size: IntegerField
    is_active: BooleanField
    content_hash: CharField
    knowledge_base_file: Union[peewee.ForeignKeyField, 'KnowledgeBaseFileTab']
    upload_records: Union[BackrefAccessor['FileUploadRecordTab'], ModelSelect['FileUploadRecordTab']]
    audio: Union[BackrefAccessor['AudioTab'], ModelSelect['AudioTab']]

    class __InnerFields(TypedDict):
        name: str
        path: str
        type: str
        extension: str
        size: int
        is_active: bool
        content_hash: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['FileTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['FileTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'FileTab':
        pass


class SearchHistoryTab(BaseModel):
    keyword: CharField
    search_ts: IntegerField
    user: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        keyword: str
        search_ts: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['SearchHistoryTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['SearchHistoryTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'SearchHistoryTab':
        pass


class AudioTab(BaseModel):
    url: CharField
    content: CharField
    message: Union[peewee.ForeignKeyField, 'MessageTab']
    file: Union[peewee.ForeignKeyField, 'FileTab']

    class __InnerFields(TypedDict):
        url: str
        content: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['AudioTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['AudioTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'AudioTab':
        pass


class TransactionTab(BaseModel):
    voucher_number: CharField
    type: CharField
    description: CharField
    account_remain_amount: DecimalField
    amount: DecimalField
    notes: CharField
    create_date: CharField
    create_at: IntegerField
    date: CharField
    timestamp: IntegerField
    account: Union[peewee.ForeignKeyField, 'AccountTab']
    transaction_item: Union[peewee.ForeignKeyField, 'TransactionItemTab']
    receivable_payable: Union[peewee.ForeignKeyField, 'ReceivablePayableTab']
    project: Union[peewee.ForeignKeyField, 'ProjectTab']
    contract: Union[peewee.ForeignKeyField, 'ContractTab']
    salary: Union[peewee.ForeignKeyField, 'SalaryTab']
    employee_loan: Union[peewee.ForeignKeyField, 'EmployeeLoanTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        voucher_number: str
        type: str
        description: str
        account_remain_amount: Decimal
        amount: Decimal
        notes: str
        create_date: str
        create_at: int
        date: str
        timestamp: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['TransactionTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['TransactionTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'TransactionTab':
        pass


class AccountTab(BaseModel):
    name: CharField
    amount: DecimalField
    create_date: CharField
    create_at: IntegerField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]
    transfer_in_records: Union[BackrefAccessor['InternalTransferTab'], ModelSelect['InternalTransferTab']]
    transfer_out_records: Union[BackrefAccessor['InternalTransferTab'], ModelSelect['InternalTransferTab']]

    class __InnerFields(TypedDict):
        name: str
        amount: Decimal
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['AccountTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['AccountTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'AccountTab':
        pass


class InternalTransferTab(BaseModel):
    amount: DecimalField
    create_date: CharField
    create_at: IntegerField
    timestamp: IntegerField
    date: CharField
    description: CharField
    target_account: Union[peewee.ForeignKeyField, 'AccountTab']
    source_account: Union[peewee.ForeignKeyField, 'AccountTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        amount: Decimal
        create_date: str
        create_at: int
        timestamp: int
        date: str
        description: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['InternalTransferTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['InternalTransferTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'InternalTransferTab':
        pass


class ReceivablePayableTab(BaseModel):
    description: CharField
    type: CharField
    amount: DecimalField
    completed_amount: DecimalField
    write_off: BooleanField
    notes: CharField
    create_date: CharField
    create_at: IntegerField
    start_date: CharField
    end_date: CharField
    timestamp: IntegerField
    date: CharField
    product_name: CharField
    specification: CharField
    quantity: IntegerField
    unit_price: DecimalField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    project: Union[peewee.ForeignKeyField, 'ProjectTab']
    employee: Union[peewee.ForeignKeyField, 'EmployeeTab']
    contract: Union[peewee.ForeignKeyField, 'ContractTab']
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]

    class __InnerFields(TypedDict):
        description: str
        type: str
        amount: Decimal
        completed_amount: Decimal
        write_off: bool
        notes: str
        create_date: str
        create_at: int
        start_date: str
        end_date: str
        timestamp: int
        date: str
        product_name: str
        specification: str
        quantity: int
        unit_price: Decimal

    @classmethod
    def select(cls, *fields) -> ModelSelect['ReceivablePayableTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['ReceivablePayableTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'ReceivablePayableTab':
        pass


class OffsetItemTab(BaseModel):
    name: CharField
    amount: DecimalField
    create_date: CharField
    create_at: IntegerField
    employee_loan: Union[peewee.ForeignKeyField, 'EmployeeLoanTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        name: str
        amount: Decimal
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['OffsetItemTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['OffsetItemTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'OffsetItemTab':
        pass


class EmployeeLoanTab(BaseModel):
    description: CharField
    amount: DecimalField
    adjustment_amount: DecimalField
    repayment_amount: DecimalField
    offset_count: DecimalField
    completed_amount: DecimalField
    create_date: CharField
    write_off: BooleanField
    create_at: IntegerField
    start_date: CharField
    end_date: CharField
    timestamp: IntegerField
    date: CharField
    employee: Union[peewee.ForeignKeyField, 'EmployeeTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    project: Union[peewee.ForeignKeyField, 'ProjectTab']
    repayment_item: Union[BackrefAccessor['OffsetItemTab'], ModelSelect['OffsetItemTab']]
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]

    class __InnerFields(TypedDict):
        description: str
        amount: Decimal
        adjustment_amount: Decimal
        repayment_amount: Decimal
        offset_count: Decimal
        completed_amount: Decimal
        create_date: str
        write_off: bool
        create_at: int
        start_date: str
        end_date: str
        timestamp: int
        date: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['EmployeeLoanTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['EmployeeLoanTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'EmployeeLoanTab':
        pass


class EmployeeTab(BaseModel):
    name: CharField
    age: IntegerField
    gender: CharField
    create_date: CharField
    create_at: IntegerField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    salary: Union[BackrefAccessor['SalaryTab'], ModelSelect['SalaryTab']]
    employee_loan: Union[BackrefAccessor['EmployeeLoanTab'], ModelSelect['EmployeeLoanTab']]
    employee_project_record: Union[BackrefAccessor['EmployeeProjectRecord'], ModelSelect['EmployeeProjectRecord']]
    receivable_payable: Union[BackrefAccessor['ReceivablePayableTab'], ModelSelect['ReceivablePayableTab']]

    class __InnerFields(TypedDict):
        name: str
        age: int
        gender: str
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['EmployeeTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['EmployeeTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'EmployeeTab':
        pass


class SupplierTab(BaseModel):
    name: CharField
    contact_name: CharField
    contact_phone: CharField
    create_date: CharField
    create_at: IntegerField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    contract: Union[BackrefAccessor['ContractTab'], ModelSelect['ContractTab']]

    class __InnerFields(TypedDict):
        name: str
        contact_name: str
        contact_phone: str
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['SupplierTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['SupplierTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'SupplierTab':
        pass


class CustomerTab(BaseModel):
    name: CharField
    contact_name: CharField
    contact_phone: CharField
    create_date: CharField
    create_at: IntegerField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    contract: Union[BackrefAccessor['ContractTab'], ModelSelect['ContractTab']]

    class __InnerFields(TypedDict):
        name: str
        contact_name: str
        contact_phone: str
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['CustomerTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['CustomerTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'CustomerTab':
        pass


class ProjectTab(BaseModel):
    name: CharField
    budget: DecimalField
    start_date: CharField
    end_date: CharField
    create_date: CharField
    create_at: IntegerField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    contract: Union[BackrefAccessor['ContractTab'], ModelSelect['ContractTab']]
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]
    employee_project_record: Union[BackrefAccessor['EmployeeProjectRecord'], ModelSelect['EmployeeProjectRecord']]
    receivable_payable: Union[BackrefAccessor['ReceivablePayableTab'], ModelSelect['ReceivablePayableTab']]
    salary: Union[BackrefAccessor['SalaryTab'], ModelSelect['SalaryTab']]
    employee_loan: Union[BackrefAccessor['EmployeeLoanTab'], ModelSelect['EmployeeLoanTab']]

    class __InnerFields(TypedDict):
        name: str
        budget: Decimal
        start_date: str
        end_date: str
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['ProjectTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['ProjectTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'ProjectTab':
        pass


class ContractTab(BaseModel):
    number: CharField
    name: CharField
    type: CharField
    amount: DecimalField
    adjustment_amount: DecimalField
    start_date: CharField
    end_date: CharField
    create_date: CharField
    create_at: IntegerField
    total_amount: DecimalField
    completed_amount: DecimalField
    schedule: DecimalField
    invoice_total_amount: DecimalField
    notes: CharField
    timestamp: IntegerField
    date: CharField
    project: Union[peewee.ForeignKeyField, 'ProjectTab']
    customer: Union[peewee.ForeignKeyField, 'CustomerTab']
    supplier: Union[peewee.ForeignKeyField, 'SupplierTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    invoice: Union[BackrefAccessor['InvoiceTab'], ModelSelect['InvoiceTab']]
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]
    receivable_payable: Union[BackrefAccessor['ReceivablePayableTab'], ModelSelect['ReceivablePayableTab']]

    class __InnerFields(TypedDict):
        number: str
        name: str
        type: str
        amount: Decimal
        adjustment_amount: Decimal
        start_date: str
        end_date: str
        create_date: str
        create_at: int
        total_amount: Decimal
        completed_amount: Decimal
        schedule: Decimal
        invoice_total_amount: Decimal
        notes: str
        timestamp: int
        date: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['ContractTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['ContractTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'ContractTab':
        pass


class InvoiceTab(BaseModel):
    amount: DecimalField
    tax_rate: DecimalField
    type: CharField
    number: CharField
    code: CharField
    content: CharField
    notes: CharField
    create_date: CharField
    create_at: IntegerField
    no_tax_amount: DecimalField
    tax_value: DecimalField
    submit_date: CharField
    timestamp: IntegerField
    date: CharField
    contract: Union[peewee.ForeignKeyField, 'ContractTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']

    class __InnerFields(TypedDict):
        amount: Decimal
        tax_rate: Decimal
        type: str
        number: str
        code: str
        content: str
        notes: str
        create_date: str
        create_at: int
        no_tax_amount: Decimal
        tax_value: Decimal
        submit_date: str
        timestamp: int
        date: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['InvoiceTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['InvoiceTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'InvoiceTab':
        pass


class SalaryTab(BaseModel):
    attendance_days: IntegerField
    basic_salary: DecimalField
    overtime_pay: DecimalField
    attendance_bonus: DecimalField
    subsidy: DecimalField
    bonus: DecimalField
    leave_deduction: DecimalField
    other_deductions: DecimalField
    create_date: CharField
    create_at: IntegerField
    payable_amount: DecimalField
    deductible_amount: DecimalField
    personal_tax: DecimalField
    net_salary: DecimalField
    completed_amount: DecimalField
    write_off: BooleanField
    start_date: CharField
    end_date: CharField
    date: CharField
    timestamp: IntegerField
    description: CharField
    employee: Union[peewee.ForeignKeyField, 'EmployeeTab']
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    project: Union[peewee.ForeignKeyField, 'ProjectTab']
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]

    class __InnerFields(TypedDict):
        attendance_days: int
        basic_salary: Decimal
        overtime_pay: Decimal
        attendance_bonus: Decimal
        subsidy: Decimal
        bonus: Decimal
        leave_deduction: Decimal
        other_deductions: Decimal
        create_date: str
        create_at: int
        payable_amount: Decimal
        deductible_amount: Decimal
        personal_tax: Decimal
        net_salary: Decimal
        completed_amount: Decimal
        write_off: bool
        start_date: str
        end_date: str
        date: str
        timestamp: int
        description: str

    @classmethod
    def select(cls, *fields) -> ModelSelect['SalaryTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['SalaryTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'SalaryTab':
        pass


class TransactionItemTab(BaseModel):
    name: CharField
    create_date: CharField
    create_at: IntegerField
    creator: Union[peewee.ForeignKeyField, 'AuthUserTab']
    transaction: Union[BackrefAccessor['TransactionTab'], ModelSelect['TransactionTab']]

    class __InnerFields(TypedDict):
        name: str
        create_date: str
        create_at: int

    @classmethod
    def select(cls, *fields) -> ModelSelect['TransactionItemTab']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['TransactionItemTab']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'TransactionItemTab':
        pass


class EmployeeProjectRecord(BaseModel):
    is_leader: BooleanField
    project: Union[peewee.ForeignKeyField, 'ProjectTab']
    employee: Union[peewee.ForeignKeyField, 'EmployeeTab']

    class __InnerFields(TypedDict):
        is_leader: bool

    @classmethod
    def select(cls, *fields) -> ModelSelect['EmployeeProjectRecord']:
        pass

    @classmethod
    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['EmployeeProjectRecord']:
        pass

    @classmethod
    def create(cls, **query: __InnerFields) -> 'EmployeeProjectRecord':
        pass

