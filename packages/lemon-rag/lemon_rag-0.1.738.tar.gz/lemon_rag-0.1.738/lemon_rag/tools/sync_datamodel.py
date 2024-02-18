import os.path
import time
from enum import Enum
from typing import Any
from typing import List, Optional, Dict

import pydantic
import requests
from pydantic import BaseModel
from pydantic import Field

from lemon_rag.configs.local_dev_config import config
from settings import BASE_DIR

base_model_file_template: str
with open(os.path.join(BASE_DIR, "lemon_rag", "lemon_runtime", "models_template.py"), "r") as template_file:
    base_model_file_template = template_file.read()


class EnumItem(BaseModel):
    name: str
    uuid: str
    color: str = "#000"
    value: str
    description: str = ""

    def __init__(self, **kwargs):
        if "value" not in kwargs and (name := kwargs.get("name")):
            kwargs.update({"value": name})

        super().__init__(**kwargs)


class EnumDeclare(BaseModel):
    name: str
    uuid: str
    value: List[EnumItem] = Field(default_factory=list)
    description: str = ""


EnumList = List[EnumDeclare]


class EnumDocument(BaseModel):
    enum_list: EnumList = Field(default_factory=list)
    uuid: str


EnumDefinition = EnumDeclare


class FieldType(int, Enum):
    AUTO = 0  # 自动
    OBJECT = 1  # 对象
    LIST = 2  # 列表
    ENUM = 3  # 枚举

    STRING = 10  # 字符
    INTEGER = 11  # 整数
    DECIMAL = 12  # 小数
    BOOLEAN = 13  # 布尔值
    DATETIME = 14  # 时间日期
    DATE = 15  # 日期
    TIME = 16  # 时间
    PHONE = 17  # 电话号码
    CURRENCY = 18  # 货币
    BYTES = 19  # 二进制
    FILE = 20  # 文件
    FIXSTRING = 21
    JSON = 22
    IMAGE = 23  # 图片
    DATETIME_CYCLE = 24  # 日期循环

    RELATION = 30  # 关联

    NOT_SUPPORT = 100

    def __str__(self):
        return self.name

    def __missing__(self, key):
        return self.NOT_SUPPORT

    def to_py_type(self):
        return {
            self.STRING: "str",
            self.INTEGER: "int",
            self.DECIMAL: "Decimal",
            self.BOOLEAN: "bool",
            self.DATETIME: "datetime",
            self.DATE: "date",
            self.ENUM: "str"
        }.get(self, "")

    def to_peewee_field(self):
        return {
            self.STRING: "CharField",
            self.INTEGER: "IntegerField",
            self.DECIMAL: "DecimalField",
            self.BOOLEAN: "BooleanField",
            self.IMAGE: "ImageField",
            self.DATETIME: "DatetimeField",
            self.DATE: "DateField",
            self.FILE: "FileField",
            self.ENUM: "CharField"
        }.get(self, "")


valid_field_types = set(t.name for t in FieldType)


class TableField(pydantic.BaseModel):
    enum: Optional[str] = ""
    name: str
    type: Optional[FieldType] = None
    uuid: str
    length: int = 300
    decimals: int = 4
    is_unique: bool = False
    is_visible: bool = True
    is_required: bool = True


class RelationshipType(str, Enum):
    ONE_TO_MANY = "0"
    MANY_TO_MANY = "1"
    ONE_TO_ONE = "2"

    def __missing__(self, key):
        return {
            "OneToOne": self.ONE_TO_ONE,
            "ForeignKey": self.ONE_TO_MANY,
            "ManyToMany": self.MANY_TO_MANY
        }.get(key, self.ONE_TO_MANY)


class Relationship(pydantic.BaseModel):
    name: str
    type: RelationshipType
    uuid: str
    source_model: str
    target_model: str
    frontref: str
    backref: str
    is_system: bool = False
    description: str = ""
    display_name: str = ""

    system_relationship: bool = False

    def __init__(self, **kwargs):
        if "display_name" not in kwargs:
            kwargs["display_name"] = kwargs.get("name", "-")
        super().__init__(**kwargs)


class Table(pydantic.BaseModel):
    uuid: str
    name: str = ""
    fields: List[TableField] = Field(default_factory=list)


class ModelDocument(pydantic.BaseModel):
    models: List[Table] = []
    relationships: List[Relationship] = []


class Document(BaseModel):
    document_type: int
    document_uuid: str
    document_name: str
    document_version: int


class DesignClient(BaseModel):
    username: str
    password: str
    token: str = ""
    base_url: str
    module_uuid: str
    app_uuid: str

    def request(self, path: str, data: Dict[str, Any], need_token: bool = True) -> dict:
        if not self.token and need_token:
            self.login()

        res = requests.post(
            self.base_url + path, json=data, headers={"Authorization": "Bearer " + self.token}
        )
        res.raise_for_status()
        res_json = res.json()
        print(path, data, res_json)
        return res_json["data"]

    def login(self):
        res = self.request("/api/auth/login.json", {
            "account": self.username,
            "code": self.password,
            "login_type": 0
        }, need_token=False)
        self.token = res["access_token"]

    def list_document(self, parent_document: str = "") -> List[Document]:
        res_json = self.request(
            "/api/ide/v1/list_document.json",
            {"app_uuid": self.app_uuid, "module_uuid": self.module_uuid, "document_uuid": parent_document}
        )
        return [Document(**d) for d in res_json["children"]]

    def get_data_model(self, document_id: str) -> ModelDocument:
        res_json = self.request(
            "/api/ide/v1/get_document_content.json",
            {"app_uuid": self.app_uuid, "document_uuid": document_id},
        )
        return ModelDocument(**res_json["document_content"])

    def create_cloud_func(self, document_name: str, document_content: dict, parent_uuid: str):
        return self.request(
            "/api/ide/v1/create_document.json",
            {
                "app_uuid": self.app_uuid,
                "module_uuid": self.module_uuid,
                "document_name": document_name,
                "document_type": "3",
                "document_puuid": parent_uuid,
                "ext_tenant": "",
                "document_content": document_content
            }
        )


def extract_data_model_document_uuid(doc_list: List[Document]) -> Document:
    return list(filter(lambda d: d.document_type == 1, doc_list))[0]


def get_model_methods_override(model: Table):
    return [
        f"    @classmethod",
        f"    def select(cls, *fields) -> ModelSelect['{model.name}']:",
        "        pass",
        "",
        f"    @classmethod",
        f"    def update(cls, __data=..., **update: __InnerFields) -> ModelUpdate['{model.name}']:",
        "        pass",
        "",
        f"    @classmethod",
        f"    def create(cls, **query: __InnerFields) -> '{model.name}':",
        "        pass"
    ]


def assemble_data_models_code(model_document: ModelDocument) -> str:
    uuid_to_table_map: Dict[str, Table] = {t.uuid: t for t in model_document.models}
    lines = []
    for model in model_document.models:
        out_relationships: List[Relationship] = [
            r for r in model_document.relationships if r.source_model == model.uuid
        ]
        back_relationships: List[Relationship] = [
            r for r in model_document.relationships if r.target_model == model.uuid
        ]
        lines.append(f"class {model.name}(BaseModel):")
        for field in model.fields:
            lines.append(f"    {field.name}: {field.type.to_peewee_field()}")

        for relationship in out_relationships:
            try:
                target_model_type = uuid_to_table_map.get(relationship.target_model).name
                lines.append(
                    f"    {relationship.frontref}: Union[peewee.ForeignKeyField, '{target_model_type}']")
            except AttributeError:
                pass

        for relationship in back_relationships:
            source_model_type = uuid_to_table_map.get(relationship.source_model).name
            lines.append(
                f"    {relationship.backref}: Union[BackrefAccessor['{source_model_type}'], ModelSelect['{source_model_type}']]")

        lines.extend([""])
        lines.append("    class __InnerFields(TypedDict):")
        for field in model.fields:
            lines.append(f"        {field.name}: {field.type.to_py_type()}")
        if not model.fields:
            lines.append("        pass")
        lines.extend([""])
        lines.extend(get_model_methods_override(model))
        lines.extend(["", ""])
    return "\n".join(lines)


def generate_data_model_stub_v2():
    clients = [DesignClient(**config.lemon_rag.dict()), DesignClient(**config.project_ledger.dict())]
    last_doc: List[Optional[Document]] = [None for _ in clients]
    while True:
        need_update = False
        combined_model_document = ModelDocument()
        for index, client in enumerate(clients):
            res = client.list_document()
            data_model_document = extract_data_model_document_uuid(res)
            if last_doc[index] is None or last_doc[index].document_version < data_model_document.document_version:
                need_update = True
            last_doc[index] = data_model_document
        if need_update:
            for index, client in enumerate(clients):

                model_document: ModelDocument = client.get_data_model(last_doc[index].document_uuid)
                combined_model_document.models.extend(model_document.models)
                combined_model_document.relationships.extend(model_document.relationships)
            with open(os.path.join(BASE_DIR, "lemon_rag", "lemon_runtime", "models.py"), "w") as f:
                f.write(base_model_file_template)
                f.write(assemble_data_models_code(combined_model_document))
        time.sleep(5)


def generate_data_model_stub():
    rag_last_doc: Optional[Document] = None
    ledger_last_doc: Optional[Document] = None
    rag_module_client = DesignClient(**config.lemon_rag.dict())
    ledger_module_client = DesignClient(**config.project_ledger.dict())
    while True:
        res = rag_module_client.list_document()
        data_model_document = extract_data_model_document_uuid(res)

        if rag_last_doc is None or rag_last_doc.document_version < data_model_document.document_version:
            model_document: ModelDocument = rag_module_client.get_data_model(data_model_document.document_uuid)
            with open(os.path.join(BASE_DIR, "lemon_rag", "lemon_runtime", "models.py"), "w") as f:
                f.write(base_model_file_template)
                f.write(assemble_data_models_code(model_document))
        rag_last_doc = data_model_document

        time.sleep(5)


if __name__ == '__main__':
    generate_data_model_stub_v2()
