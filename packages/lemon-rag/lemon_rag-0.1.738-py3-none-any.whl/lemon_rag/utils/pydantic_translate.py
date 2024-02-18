from pydantic_i18n import PydanticI18n

translations = {
    "zh_CN": {
        "field required": "该字段为必填"
    }
}
tr = PydanticI18n(translations)