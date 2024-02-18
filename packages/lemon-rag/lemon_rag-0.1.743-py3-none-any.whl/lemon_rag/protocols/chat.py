import abc
import datetime
import decimal
import uuid
from enum import Enum
from typing import Optional, List, Any, Union, Dict, Generic, TypeVar

from pydantic import BaseModel, Field, validator
from typing_extensions import Annotated, Literal

from lemon_rag.llm.agents.rag.vectorization.content_extractor import split_text

T = TypeVar('T')


def get_uuid():
    return uuid.uuid4().hex


class RatingType(int, Enum):
    LIKE = 1
    DISLIKE = -1
    NONE = 0

    @classmethod
    def __missing__(cls, key):
        return cls.NONE


class BusinessDataType(str, Enum):
    transaction = "收入和支出的交易记录"
    internal_transfer = "内部账户转账记录"
    receivable_payable = "应收应付记录"
    employee_loan = "员工借款记录"
    employee_salary = "员工工资记录"
    contract = "合同信息"
    invoice = "发票信息"

    employee = "员工信息"
    project = "项目信息"
    account = "账户信息"
    supplier = "供应商"
    customer = "客户"

    def api_sub_path(self) -> str:
        api_path_mapping: Dict = {
            self.transaction: 'save_transaction_record',
            self.employee_loan: 'save_employee_loan_bill',
            self.employee_salary: 'save_employee_salary_bill',
            self.receivable_payable: 'save_receivable_payable_bill',
            self.internal_transfer: 'save_internal_transfer_record',
            self.employee: 'save_employee_info',
            self.account: 'save_account_info',
            self.project: 'save_project_info',
            self.contract: 'save_contract_info',
            self.invoice: 'save_invoice_info',
            self.supplier: 'save_supplier_info',
            self.customer: 'save_customer_info',
        }
        return api_path_mapping.get(self, "")


class BusinessType(str, Enum):
    transaction_item = "transaction_item"
    contract = "contract"
    receivable_payable = "receivable_payable"
    employee_loan = "employee_loan"
    salary = "salary"
    supplier = "supplier"
    customer = "customer"

    employee = "employee"
    project = "project"
    account = "account"


class Embeddable(abc.ABC):
    @abc.abstractmethod
    def embed_keys(self) -> List[str]:
        pass


class KnowledgeBase(BaseModel):
    id: int
    name: str


class RefFile(BaseModel):
    id: int
    knowledge_base_file_id: Optional[int]
    origin_filename: str
    url: str
    extension: str
    file_size: int
    paragraph_id_list: List[int] = []


class RefFileWithContent(RefFile):
    content: List[str] = []


class ChatRole(str, Enum):
    assistant = "assistant"
    notification_center = "notification_center"
    standard_query = "standard_query"
    user = "user"


class Session(BaseModel):
    id: int
    topic: str
    title: str
    messages: Optional[List['Message']]
    latest_msg_ts: Optional[int]
    role: str
    create_at: int
    version: int


class Message(BaseModel):
    id: int
    msg_id: int
    role: str
    text: str
    client_ts: int
    server_ts: int
    content: str
    msg_signature: Optional[str]
    rating: RatingType = RatingType.NONE
    user_msg_id: Optional[int]

    @validator('rating', pre=True, always=True)
    def set_default_rating(cls, rating):
        if rating == "" or rating is None:
            return RatingType.NONE
        return rating


class CompleteMessage(Message):
    context_text: str
    is_system: bool
    is_answer: bool
    is_system_msg: bool
    support_retry: bool
    support_rating: bool
    version: int


class CardComponentType(str, Enum):
    TEXT = "text"
    PROJECT_CARD = "project_card"
    REFERENCE = "reference"
    FILE = "file"
    AUDIO = "audio"
    GUIDE_CARD = "guide_card"
    TRANSACTION = "transaction"
    SUM = "sum"
    FORM = "form"
    BUTTON = "button"


class ClickAction(str, Enum):
    after_upload_knowledgebase_file = "after_upload_knowledgebase_file"
    after_form_submit = "after_form_submit"


class TextComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.TEXT] = CardComponentType.TEXT
    data: str

    def embed_keys(self) -> List[str]:
        return split_text(self.data)


class ReferenceData(BaseModel):
    ref_files: List[RefFile]


class RefComponent(BaseModel, Embeddable):
    def embed_keys(self) -> List[str]:
        return [
            f"引用了文件：{f.origin_filename}" for f in self.data.ref_files
        ]

    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.REFERENCE] = CardComponentType.REFERENCE
    data: ReferenceData


class FileComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.FILE] = CardComponentType.FILE
    data: RefFile

    def embed_keys(self) -> List[str]:
        return [f"上传了文件：{self.data.origin_filename}"]


class ResourceData(BaseModel):
    resource_id: str


class FormKVPair(BaseModel):
    key: str
    value: Union[str, int]


class FileSettings(BaseModel):
    pass


class DependencyType(str, Enum):
    FORM_FIELD = "form_field"
    CONST = "const"


class CompareRule(str, Enum):
    EQUAL = "equal"
    GREATER = "greater"
    LESS = "less"
    GREATER_EQUAL = "greater_equal"
    LESS_EQUAL = "less_equal"


class VisibleCondition(BaseModel, Generic[T]):
    depend_on: DependencyType = DependencyType.FORM_FIELD
    compare_rule: CompareRule = CompareRule.EQUAL
    target_key: str
    target_value: T


class ConditionOperator(BaseModel):
    pass


class ConditionalField(BaseModel):
    conditions: List[Union[VisibleCondition, ConditionOperator]]
    fields: List['FormFieldSchema']
    default: Optional['FormFieldSchema']


class ConditionalSettings(BaseModel):
    fields: List[ConditionalField]


class OptionPair(BaseModel):
    label: str
    value: Union[str, int]


class Dependency(BaseModel):
    name: str
    value: Optional[str]
    type: Optional[BusinessType]
    dependency_type: DependencyType = DependencyType.FORM_FIELD


class OptionsParam(BaseModel):
    type: BusinessType
    keyword: Optional[str]
    dependencies: List[Dependency] = Field(default_factory=list)


class SelectSettings(BaseModel):
    options_params: Optional[OptionsParam]
    multiple: bool = False
    options: List[OptionPair] = Field(default_factory=list)


class InputSettings(BaseModel):
    min_length: int = 0
    max_length: int = 300


class NumberSettings(BaseModel):
    min: Optional[Union[int, float]]
    max: Optional[Union[int, float]]


class MoneySettings(BaseModel):
    unit: str = "元"


class SwitchSettings(BaseModel):
    default: bool


# 是否展示日期
class DatetimeSettings(BaseModel):
    select_time: bool = True


class FormControlComponent(str, Enum):
    INPUT = "input"
    DATETIME = "datetime"
    SWITCH = "switch"
    MONEY = "money"
    NUMBER = "number"
    SELECT = "select"
    CONDITION = "condition"


FieldSettings = Union[
    NumberSettings, InputSettings, SelectSettings,
    DatetimeSettings, FileSettings, SwitchSettings,
    MoneySettings, DatetimeSettings, ConditionalSettings
]


class BaseFormFieldSchema(BaseModel):
    db_field_name: str
    name: str
    label: str
    required: bool = True
    editable: bool = True
    control_component: FormControlComponent

    def get_default_value(self) -> Optional[str]:
        return {
            FormControlComponent.INPUT: "",
            FormControlComponent.DATETIME: datetime.datetime.now().strftime("%Y年%m月%d日"),
            FormControlComponent.MONEY: "0",
            FormControlComponent.NUMBER: 0,
            FormControlComponent.SWITCH: False,
            FormControlComponent.SELECT: "",
            FormControlComponent.CONDITION: ""
        }.get(self.control_component)


class ConditionalFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.CONDITION] = FormControlComponent.CONDITION
    field_settings: ConditionalSettings


class SelectFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.SELECT] = FormControlComponent.SELECT
    field_settings: SelectSettings


class NumberFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.NUMBER] = FormControlComponent.NUMBER
    field_settings: NumberSettings


class MoneyFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.MONEY] = FormControlComponent.MONEY
    field_settings: MoneySettings


class InputFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.INPUT] = FormControlComponent.INPUT
    field_settings: InputSettings


class DatetimeFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.DATETIME] = FormControlComponent.DATETIME
    field_settings: DatetimeSettings


class SwitchFieldSchema(BaseFormFieldSchema):
    control_component: Literal[FormControlComponent.SWITCH] = FormControlComponent.SWITCH
    field_settings: SwitchSettings


FormFieldSchema = Annotated[
    Union[
        SelectFieldSchema, NumberFieldSchema, MoneyFieldSchema, DatetimeFieldSchema, InputFieldSchema,
        SwitchFieldSchema, ConditionalFieldSchema
    ],
    Field(discriminator="control_component")
]


class FormSchema(BaseModel):
    type: BusinessDataType
    fields: List[FormFieldSchema] = Field(default_factory=list)

    # TODO 优化：可以把map初始化写到属性中

    def to_db_value_map(self, kv_pairs: List[FormKVPair]) -> Dict[str, Union[str, int]]:
        # name: value -> db_name: value
        kv_pairs_dict = {pair.key: pair.value for pair in kv_pairs}
        db_map: Dict[str, Union[str, int]] = {}
        for field in self.fields:
            if field.control_component == FormControlComponent.CONDITION:
                for condition_field in field.field_settings.fields:
                    for condition_f in condition_field.fields:
                        db_map[condition_f.db_field_name] = kv_pairs_dict.get(condition_f.name, "")
            else:
                db_map[field.db_field_name] = kv_pairs_dict.get(field.name, "")
        return db_map

    def get_name_by_db_field_name(self, db_field_name: str) -> str:
        for field in self.fields:
            if field.control_component == FormControlComponent.CONDITION:
                for condition_field in field.field_settings.fields:
                    for condition_f in condition_field.fields:
                        if condition_f.db_field_name == db_field_name:
                            return condition_f.name
            else:
                if field.db_field_name == db_field_name:
                    return field.name
        return ""

    def get_db_field_name_by_name(self, name: str) -> str:
        for field in self.fields:
            if field.control_component == FormControlComponent.CONDITION:
                for condition_field in field.field_settings.fields:
                    for condition_f in condition_field.fields:
                        if condition_f.name == name:
                            return condition_f.db_field_name
            else:
                if field.name == name:
                    return field.db_field_name
        return ""


class Member(BaseModel):
    id: int
    name: str
    avatar: str


class ProjectCardData(BaseModel):
    id: int
    name: str
    days_remained: int
    total_stage: int
    current_stage: int
    members: List[Member]
    incoming: decimal.Decimal = Field(decimal_places=2)
    out_coming: decimal.Decimal = Field(decimal_places=2)
    balance: decimal.Decimal = Field(decimal_places=2)


class ProjectCardComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.PROJECT_CARD] = CardComponentType.PROJECT_CARD
    data: ProjectCardData

    def embed_keys(self) -> List[str]:
        return [f"{self.data.name}项目信息概览"]


class FormData(BaseModel):
    submitted: bool = False  # 是否已经提交
    form_schema: FormSchema
    filled_data: List[FormKVPair] = []


class FormComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.FORM] = CardComponentType.FORM
    data: FormData

    def embed_keys(self) -> List[str]:
        value_map = {item.key: item.value for item in self.data.filled_data if isinstance(item.value, str)}
        return [f"填写{self.data.form_schema.type.value}的表单 填写结果：{value_map}"]


class AudioData(BaseModel):
    audio_id_list: List[int]


class AudioComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.AUDIO] = CardComponentType.AUDIO
    data: AudioData

    def embed_keys(self) -> List[str]:
        return []


class GuideCardItem(BaseModel):
    title: str
    icon: str
    text: str
    callback: List['CallbackMethod']


class GuideCardData(BaseModel):
    title: str
    card_items: List[GuideCardItem]


class GuideCardComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.GUIDE_CARD] = CardComponentType.GUIDE_CARD
    data: GuideCardData

    def embed_keys(self) -> List[str]:
        return [f"新用户指引卡片"]


class Tag(BaseModel):
    value: str
    fill: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if len(self.value) > 10:
            self.value = f'{self.value[:10]}...'


class TransactionData(BaseModel):
    id: int
    trx_code: str = ""  # uuid或者用户提供的
    title: str
    amount: decimal.Decimal = Field(decimal_places=2)  # 金额
    tags: List[Tag]
    datetime: str  # xxxx年xx月xx日
    datetime_label: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if len(self.title) > 8:
            self.title = f'{self.title[:8]}...'


class TransactionComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.TRANSACTION] = CardComponentType.TRANSACTION
    data: TransactionData

    def embed_keys(self) -> List[str]:
        if self.data.amount >= 0:
            return [f"转入记录{self.data.title} 金额：{self.data.amount} 标签: {self.data.tags}"]
        else:
            return [f"转出记录{self.data.title} 金额：{self.data.amount} 标签：{self.data.tags}"]


class SumData(BaseModel):
    project_name: str
    out_coming: str
    incoming: str
    balance: str


class SumComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.SUM] = CardComponentType.SUM
    data: SumData

    def embed_keys(self) -> List[str]:
        return [f"{self.data.project_name}项目资金概览"]


class ButtonType(str, Enum):
    default = "default"
    primary = "primary"


class CardCallbackAction(str, Enum):
    UPLOAD_KNOWLEDGE_BASE_FILE = "upload_knowledge_base_file"
    CLICK_BUTTON_EVENT = "click_button_event"
    SAVE_FORM = "save_form"


class CallbackMethod(BaseModel):
    action: CardCallbackAction
    params: Dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def handle_form(cls, path: str):
        return CallbackMethod(action=CardCallbackAction.SAVE_FORM, params={
            "path": path,
        })

    @classmethod
    def update_button(cls, session_id: int, msg_id: int, action: ClickAction):
        return CallbackMethod(action=CardCallbackAction.CLICK_BUTTON_EVENT, params={
            "msg_id": msg_id, "session_id": session_id,
            "action": action
        })


class ButtonData(BaseModel):
    text: str
    callback: List[CallbackMethod]
    type_: ButtonType = ButtonType.primary


class ButtonComponent(BaseModel, Embeddable):
    id: str = Field(default_factory=get_uuid)
    type: Literal[CardComponentType.BUTTON] = CardComponentType.BUTTON
    data: ButtonData

    def embed_keys(self) -> List[str]:
        return []


CardComponent = Annotated[
    Union[
        TextComponent, ProjectCardComponent, RefComponent, FileComponent, AudioComponent, GuideCardComponent,
        TransactionComponent, SumComponent, FormComponent, ButtonComponent,
    ],
    Field(discriminator="type")
]


class CardMessage(BaseModel):
    components: List[CardComponent] = Field(default_factory=list)
    text_component: Optional[TextComponent] = Field(default=None, exclude=True)
    ref_component: Optional[RefComponent] = Field(default=None, exclude=True)
    file_component: Optional[FileComponent] = Field(default=None, exclude=True)
    project_card_component: Optional[ProjectCardComponent] = Field(default=None, exclude=True)
    audio_component: Optional[AudioComponent] = Field(default=None, exclude=True)
    guide_card_component: Optional[GuideCardComponent] = Field(default=None, exclude=True)
    transaction_component: Optional[TransactionComponent] = Field(default=None, exclude=True)
    sum_component: Optional[SumComponent] = Field(default=None, exclude=True)
    button_component: Optional[ButtonComponent] = Field(default=None, exclude=True)
    form_component: Optional[FormComponent] = Field(default=None, exclude=True)

    def remove_all_button(self):
        self.components = list(filter(lambda c: c.type != CardComponentType.BUTTON, self.components))
        self.button_component = None
        return self

    def append_text(self, content: str) -> 'CardMessage':
        if self.text_component is None:
            text = TextComponent(data=content)
            self.text_component = text
            self.components.append(self.text_component)
        else:
            self.text_component.data += content
        return self

    def add_text(self, content: str) -> 'CardMessage':
        text = TextComponent(data=content)
        self.text_component = text
        self.components.append(self.text_component)
        return self

    def add_project(self, data: ProjectCardData) -> 'CardMessage':
        project_card = ProjectCardComponent(data=data)
        self.project_card_component = project_card
        self.components.append(self.project_card_component)
        return self

    def add_ref_file(self, ref_file: List[RefFile]) -> 'CardMessage':
        ref = RefComponent(data=ReferenceData(ref_files=ref_file))
        self.ref_component = ref
        self.components.append(self.ref_component)
        return self

    def add_file(self, file: RefFile) -> 'CardMessage':
        file = FileComponent(data=file)
        self.file_component = file
        self.components.append(self.file_component)
        return self

    def add_audio(self, audio_id: int) -> 'CardMessage':
        if self.audio_component is None:
            audio = AudioComponent(data=AudioData(audio_id_list=[audio_id]))
            self.audio_component = audio
            self.components.append(self.audio_component)
        else:
            self.audio_component.data.audio_id_list.append(audio_id)
        return self

    def add_guide_card(self, guide_data: GuideCardData) -> 'CardMessage':
        guide_card = GuideCardComponent(data=guide_data)
        self.guide_card_component = guide_card
        self.components.append(self.guide_card_component)
        return self

    def add_transaction_card(self, transaction_data: TransactionData) -> 'CardMessage':
        transaction_card = TransactionComponent(data=transaction_data)
        self.transaction_component = transaction_card
        self.components.append(self.transaction_component)
        return self

    def add_sum_card(self, sum_data: SumData) -> 'CardMessage':
        sum_card = SumComponent(data=sum_data)
        self.sum_component = sum_card
        self.components.append(self.sum_component)
        return self

    def add_form(self, form: FormComponent) -> 'CardMessage':
        self.form_component = form
        self.components.append(self.form_component)
        return self

    def add_form_data(self, form_data: FormKVPair) -> 'CardMessage':
        self.form_component.data.filled_data.append(form_data)
        return self

    def add_button(
            self,
            text: str,
            callback: List[CallbackMethod],
            type_: ButtonType = ButtonType.primary
    ) -> 'CardMessage':
        button = ButtonComponent(type=CardComponentType.BUTTON,
                                 data=ButtonData(text=text, callback=callback, type_=type_))
        self.button_component = button
        self.components.append(self.button_component)
        return self


class MessageChunkAction(int, Enum):
    base_message = 0
    append_text = 1
    add_file = 2
    add_ref_file = 3
    add_form_schema = 4
    add_form_data = 5
    add_button = 6
    add_project_card = 7
    add_guide_card = 8
    add_transaction_card = 9
    add_sum_card = 10
    add_audio = 11
    update_form_field_schema = 12


class FillFormData(BaseModel):
    form_id: str
    data: List[FormKVPair]


class UpdateFormFieldSchema(BaseModel):
    form_id: str
    field_schema: FormFieldSchema


class ResponseChunk(BaseModel):
    action: MessageChunkAction
    session_id: int
    msg_id: int
    data: Any

    @classmethod
    def base_message(cls, session_id: int, msg_id: int, message: CompleteMessage) -> 'ResponseChunk':
        return ResponseChunk(action=MessageChunkAction.base_message, data=message, session_id=session_id, msg_id=msg_id)

    @classmethod
    def add_text(
            cls, session_id: int, msg_id: int, value: Union[str], card: CardMessage, append: bool = True
    ) -> 'ResponseChunk':
        if append:
            card = card.append_text(value)
        else:
            card = card.add_text(value)
        return ResponseChunk(
            action=MessageChunkAction.append_text,
            data=TextComponent(id=card.text_component.id, data=value),
            session_id=session_id,
            msg_id=msg_id
        )

    @classmethod
    def add_project_card(cls, session_id: int, msg_id: int, data: ProjectCardData,
                         card: CardMessage) -> 'ResponseChunk':
        card = card.add_project(data)
        return ResponseChunk(
            session_id=session_id,
            msg_id=msg_id,
            data=ProjectCardComponent(id=card.project_card_component.id, data=data),
            action=MessageChunkAction.add_project_card
        )

    @classmethod
    def add_ref_file(
            cls, session_id: int, msg_id: int, ref_files: List[RefFile], card: CardMessage
    ) -> 'ResponseChunk':
        ref_files_without_content = []
        for ref_file in ref_files:
            if isinstance(ref_file, RefFileWithContent):
                ref_file = RefFile(**ref_file.dict())
            ref_files_without_content.append(ref_file)
        card = card.add_ref_file(ref_files_without_content)
        return ResponseChunk(
            action=MessageChunkAction.add_ref_file,
            data=RefComponent(id=card.ref_component.id, data=ReferenceData(ref_files=ref_files_without_content)),
            session_id=session_id, msg_id=msg_id
        )

    @classmethod
    def add_file(
            cls, session_id: int, msg_id: int, file: RefFile, card: CardMessage) -> 'ResponseChunk':
        card = card.add_file(file)
        return ResponseChunk(
            action=MessageChunkAction.add_file,
            data=FileComponent(id=card.file_component.id, data=file),
            session_id=session_id,
            msg_id=msg_id
        )

    @classmethod
    def add_audio(cls, session_id: int, msg_id: int, audio_id: int, card: CardMessage) -> 'ResponseChunk':
        card = card.add_audio(audio_id)
        return ResponseChunk(
            action=MessageChunkAction.add_audio,
            data=AudioComponent(id=card.audio_component.id, data=AudioData(audio_id_list=[audio_id])),
            session_id=session_id, msg_id=msg_id
        )

    @classmethod
    def add_guide_card(cls, session_id: int, msg_id: int, data: GuideCardData, card: CardMessage) -> 'ResponseChunk':
        card = card.add_guide_card(guide_data=data)
        return ResponseChunk(
            action=MessageChunkAction.add_guide_card,
            session_id=session_id,
            msg_id=msg_id,
            data=GuideCardComponent(id=card.guide_card_component.id, data=data)
        )

    @classmethod
    def add_transaction_card(cls, session_id: int, msg_id: int, data: TransactionData,
                             card: CardMessage) -> 'ResponseChunk':
        card = card.add_transaction_card(transaction_data=data)
        return ResponseChunk(
            action=MessageChunkAction.add_transaction_card,
            session_id=session_id,
            msg_id=msg_id,
            data=TransactionComponent(id=card.transaction_component.id, data=data)
        )

    @classmethod
    def add_sum_card(cls, session_id: int, msg_id: int, data: SumData, card: CardMessage) -> 'ResponseChunk':
        card = card.add_sum_card(sum_data=data)
        return ResponseChunk(
            action=MessageChunkAction.add_sum_card,
            session_id=session_id,
            msg_id=msg_id,
            data=SumComponent(id=card.sum_component.id, data=data)
        )

    @classmethod
    def add_form(cls, session_id: int, msg_id: int, form: FormComponent,
                 card: CardMessage) -> 'ResponseChunk':
        card.add_form(form)
        return ResponseChunk(
            action=MessageChunkAction.add_form_schema,
            session_id=session_id,
            msg_id=msg_id,
            data=form
        )

    @classmethod
    def set_form_data(cls, session_id: int, msg_id: int, form: FormComponent,
                      data: List[FormKVPair]) -> 'ResponseChunk':
        form.data.filled_data.extend(data)
        return ResponseChunk(
            action=MessageChunkAction.add_form_data,
            session_id=session_id,
            msg_id=msg_id,
            data=FillFormData(form_id=form.id, data=data)
        )

    @classmethod
    def update_field_schema(cls, session_id: int, msg_id: int, form_id: str, field: FormFieldSchema):
        return ResponseChunk(
            action=MessageChunkAction.update_form_field_schema,
            session_id=session_id,
            msg_id=msg_id,
            data=UpdateFormFieldSchema(
                form_id=form_id,
                field_schema=field
            )
        )

    @classmethod
    def add_button(cls, session_id: int, msg_id: int, text: str, callback: List[CallbackMethod],
                   card: CardMessage, type_: ButtonType = ButtonType.primary) -> 'ResponseChunk':
        card = card.add_button(text, callback, type_)
        return ResponseChunk(
            action=MessageChunkAction.add_button,
            session_id=session_id,
            msg_id=msg_id,
            data=ButtonComponent(
                id=card.button_component.id, data=ButtonData(text=text, callback=callback, type_=type_))
        )


class File(BaseModel):
    id: int
    name: str
    path: str
    type: str
    extension: str
    size: int
    is_active: bool
    content_hash: str


class SearchHistory(BaseModel):
    keyword: str
    search_ts: int


class Paragraph(BaseModel):
    id: int
    content: str


class Form(BaseModel):
    id: str
    type: BusinessDataType
    data: List[FormKVPair]


class FormValidationError(BaseModel):
    form_id: str
    name: str
    error: str


ConditionalField.update_forward_refs()
