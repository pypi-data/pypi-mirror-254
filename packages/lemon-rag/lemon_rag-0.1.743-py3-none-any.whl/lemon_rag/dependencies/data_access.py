import decimal
import re
import time
import uuid
from datetime import datetime
from enum import Enum
from typing import Tuple, Optional, List, Iterable, Dict, TypeVar, Any, Type

import peewee
from playhouse.shortcuts import model_to_dict

from lemon_rag.lemon_runtime import models
from lemon_rag.llm.agents.rag.vectorization.content_extractor import Paragraph
from lemon_rag.protocols.business import ContractInfo, InvoiceInfo, SalaryBill, LoanBill, TransactionRecord, \
    ReceivablePayableBill
from lemon_rag.protocols.business_enum import GenderType, ReceivablePayableType, TransactionType
from lemon_rag.protocols.chat import ChatRole, CardMessage, TextComponent, RatingType
from lemon_rag.utils import log

Model_T = TypeVar('Model_T', bound=peewee.Model)


class KnowledgeBasePermission(int, Enum):
    read = 1
    write = 1 << 1
    read_write = read | write


class FileType(str, Enum):
    IMAGE = "image"
    PDF = "pdf"
    DOC = "doc"
    TXT = "txt"
    AUDIO = "audio"


class GetHistoryType(str, Enum):
    BEFORE = "before"
    AFTER = "after"


class DataAccess:

    def generate_new_auth_token(
            self, auth_user: models.AuthUserTab, expire: int = 60 * 60 * 24 * 100) -> models.AppAuthTokenTab:
        token = uuid.uuid4().hex
        token = models.AppAuthTokenTab.create(**{
            "token": token,
            "user": auth_user,
            "created_at": int(time.time()),
            "expire_at": int(time.time()) + expire
        })
        return token

    def delete_token_by_user(self, token: str, user: models.AppAuthTokenTab) -> int:
        return (models.AppAuthTokenTab.delete()
                .where(models.AppAuthTokenTab.token == token, models.AppAuthTokenTab.user == user)
                .execute())

    def delete_expired_token(self):
        current_time = int(time.time())
        models.AppAuthTokenTab.delete().where(models.AppAuthTokenTab.expire_at < current_time).execute()

    def get_or_create_session(self, user: models.AuthUserTab, role: ChatRole) -> Tuple[models.SessionTab, bool]:
        title = "AI助手" if role == ChatRole.assistant else "规范速查" if role == ChatRole.standard_query else "通知中心"
        try:
            session = models.SessionTab.get(user=user, role=role)
            create = False
        except models.SessionTab.DoesNotExist:
            session = models.SessionTab.create(**{
                "user": user,
                "role": role,
                "created_at": int(time.time()),
                "topic": "",
                "title": title,
                "last_msg_id": 0,
                "last_msg_ts": int(time.time())
            }
                                               )
            create = True
        if create:
            models.SyncHistoryTab.create(**{
                "session": session,
                "last_read_id": 0,
                "last_read_ts": int(time.time())
            })

        return session, create

    def read_message(self, session: models.SessionTab, read_id: int) -> int:
        return models.SyncHistoryTab.update(
            **{"last_read_id": read_id, "last_read_ts": int(time.time())}
        ).where(models.SyncHistoryTab.session == session).execute()

    def get_message_count(self, session: models.SessionTab) -> int:
        query = (models.MessageTab
                 .select(models.MessageTab.session, peewee.fn.Count(models.MessageTab.msg_id).alias('count'))
                 .group_by(models.MessageTab.session).where(models.MessageTab.session == session).first())
        return query.count if query else 0

    def init_account(self, user: models.AuthUserTab):
        kb = self.create_knowledge_base(
            user, "默认知识库", 100
        )
        log.info("created default knowledge base id=%s for the user=%s", kb, user)

        quota = models.UserQuotaTab.create(**{
            "auth_user": user,
            "request_per_min": 2,
            "request_per_day": 240,
            "request_per_month": 5000,
            "max_files": 100,
            "max_single_file_size": 1024 * 1024 * 5,
            "max_total_knowledge_size": 1025 * 1024 * 1024,
        })
        log.info("created default quota id=%s for the user=%s", quota, user)

    def create_knowledge_base(self, user: models.AuthUserTab, name: str, max_files: int) -> models.KnowledgeBaseTab:
        kb = models.KnowledgeBaseTab.create(**{
            "name": name,
            "owner": user,
            "max_files": max_files,
            "created_at": int(time.time())
        })
        models.KnowledgeBaseAccessTab.create(
            **{
                "permission": KnowledgeBasePermission.read_write,
                "create_at": int(time.time()),
                "user": user,
                "knowledge_base": kb,
                "creator": user
            },
        )
        return kb

    def get_knowledge_base_by_id(self, kb_id: int) -> Optional[models.KnowledgeBaseTab]:
        return models.KnowledgeBaseTab.get_or_none(kb_id)

    def get_knowledge_base_by_name(self, kb_name: str, user: models.AuthUserTab) -> Optional[models.KnowledgeBaseTab]:
        return models.KnowledgeBaseTab.get_or_none(name=kb_name, owner=user)

    def list_knowledge_base_by_user(self, user: models.AuthUserTab) -> Iterable[models.KnowledgeBaseTab]:
        return models.KnowledgeBaseTab.select().where(models.KnowledgeBaseTab.owner == user)

    def delete_knowledge_base_by_id_user(self, knowledge_base_id: int, user: models.AuthUserTab) -> int:
        return (models.KnowledgeBaseTab.delete()
                .where(models.KnowledgeBaseTab.id == knowledge_base_id, models.KnowledgeBaseTab.owner == user)
                .execute())

    def delete_knowledge_base_file_link_by_file_id(self, file_id: int, user: models.AuthUserTab) -> int:
        file = models.FileTab.get_or_none(file_id)
        knowledge_file: models.KnowledgeBaseFileTab = file.knowledge_base_file
        file_links = (models.KnowledgebaseFileLink.select()
                      .join(models.KnowledgeBaseTab)
                      .where(models.KnowledgebaseFileLink.file == knowledge_file,
                             models.KnowledgeBaseTab.owner == user))
        delete_num: int = 0
        for file_link in file_links:
            delete_num += (models.KnowledgebaseFileLink.delete()
                           .where(models.KnowledgebaseFileLink.id == file_link.id)
                           .execute())
        return delete_num

    def upload_file_by_hash(
            self, user: models.AuthUserTab, hash_value: str, kb: Optional[models.KnowledgeBaseTab] = None
    ) -> Tuple[Optional[models.FileTab], bool]:
        k_file: Optional[models.KnowledgeBaseFileTab] = None
        file: Optional[models.FileTab] = models.FileTab.get_or_none(content_hash=hash_value)
        if not file:
            return None, True
        if kb:
            k_file = models.KnowledgeBaseFileTab.get_or_none(content_hash=hash_value)
            if not k_file or file.knowledge_base_file != k_file:
                return None, False
            models.KnowledgebaseFileLink.create(**{
                "file": k_file,
                "knowledgebase": kb
            })
        models.FileUploadRecordTab.create(**{
            "upload_time": int(time.time()),
            "file": k_file,
            "upload_file": file,
            "uploader": user,
            "first_upload": False
        })
        return file, False

    def get_knowledge_file_by_id(self, file_id: int) -> Optional[models.KnowledgeBaseFileTab]:
        return models.KnowledgeBaseFileTab.get_or_none(file_id)

    def list_knowledge_file_by_knowledge_base(
            self, knowledge_base: models.KnowledgeBaseTab) -> Iterable[models.KnowledgeBaseFileTab]:
        return (models.KnowledgeBaseFileTab
                .select()
                .join(models.KnowledgebaseFileLink)
                .where(models.KnowledgebaseFileLink.knowledgebase == knowledge_base)
                .distinct()
                .execute())

    def get_file_by_id_user(self, file_id: int, user: models.AuthUserTab) -> Optional[models.FileTab]:
        return (models.FileTab.select()
                .join(models.FileUploadRecordTab)
                .where(models.FileTab.id == file_id, models.FileUploadRecordTab.uploader == user)
                .distinct()
                .first())

    def get_file_by_hash_user(self, file_hash: str, user: models.AuthUserTab) -> Optional[models.FileTab]:
        return (models.FileTab.select()
                .join(models.FileUploadRecordTab)
                .where(models.FileTab.content_hash == file_hash, models.FileUploadRecordTab.uploader == user)
                .distinct()
                .first())

    def get_file_by_knowledge_base_file(
            self, knowledge_base_file: models.KnowledgeBaseFileTab) -> Optional[models.FileTab]:
        return models.FileTab.get_or_none(knowledge_base_file=knowledge_base_file)

    def get_knowledge_base_access(
            self,
            user: models.AuthUserTab,
            kb: models.KnowledgeBaseTab
    ) -> Optional[models.KnowledgeBaseAccessTab]:
        try:
            return (
                models
                .KnowledgeBaseAccessTab
                .select()
                .where(
                    models.KnowledgeBaseAccessTab.knowledge_base == kb,
                    models.KnowledgeBaseAccessTab.user == user
                )
                .get()
            )
        except models.KnowledgeBaseAccessTab.DoesNotExist:
            return None

    def get_knowledge_base_file_count(self, kb: models.KnowledgeBaseTab) -> int:
        return kb.file_links.select(peewee.fn.Count(peewee.SQL("1"))).scalar()

    def create_knowledge_file(
            self,
            filename: str,
            extension: str,
            origin_filename: str,
            file_size: int,
            content_hash: str,
            is_create_file: bool,
            kb: models.KnowledgeBaseTab,
            user: models.AuthUserTab
    ) -> Tuple[models.KnowledgeBaseFileTab, models.FileTab]:
        file_type_mapping: Dict[str, FileType] = {
            "txt": FileType.TXT, "pdf": FileType.PDF, "png": FileType.IMAGE, "jpg": FileType.IMAGE,
            "jpeg": FileType.IMAGE, "docx": FileType.DOC, "doc": FileType.DOC, "mp3": FileType.AUDIO
        }
        knowledge_file = models.KnowledgeBaseFileTab.create(**{
            "filename": filename,
            "extension": extension,
            "origin_filename": origin_filename,
            "file_size": file_size,
            "total_parts": 0,
            "vectorized_parts": 0,
            "content_hash": content_hash
        })
        # 同步一份到file
        if is_create_file:
            file = models.FileTab.create(**{
                "name": origin_filename,
                "path": filename,
                "type": file_type_mapping.get(extension),
                "extension": extension,
                "size": file_size,
                "is_active": True,
                "content_hash": content_hash,
                "knowledge_base_file": knowledge_file
            })
        else:
            file = data_access.get_file_by_hash_user(content_hash, user)
            (models.FileTab.update(**{"knowledge_base_file": knowledge_file})
             .where(models.FileTab.content_hash == content_hash)
             .execute())
        models.KnowledgebaseFileLink.create(**{
            "file": knowledge_file,
            "knowledgebase": kb
        })
        models.FileUploadRecordTab.create(**{
            "upload_time": int(time.time()),
            "file": knowledge_file,
            "upload_file": file,
            "uploader": user,
            "first_upload": True
        })

        return knowledge_file, file

    def create_file(
            self,
            filename: str,
            extension: str,
            path: str,
            file_size: int,
            content_hash: str,
            user: models.AuthUserTab
    ) -> models.FileTab:
        file_type_mapping: Dict[str, FileType] = {
            "txt": FileType.TXT, "pdf": FileType.PDF, "png": FileType.IMAGE, "jpg": FileType.IMAGE,
            "jpeg": FileType.IMAGE, "docx": FileType.DOC, "doc": FileType.DOC, "mp3": FileType.AUDIO
        }
        file = models.FileTab.create(**{
            "name": filename,
            "path": path,
            "type": file_type_mapping.get(extension),
            "extension": extension,
            "size": file_size,
            "is_active": True,
            "content_hash": content_hash
        })
        models.FileUploadRecordTab.create(**{
            "upload_time": int(time.time()),
            "upload_file": file,
            "uploader": user,
            "first_upload": True
        })
        return file

    def create_paragraphs(
            self,
            file: models.KnowledgeBaseFileTab,
            paragraphs: List[Paragraph]
    ) -> List[models.KnowledgeParagraph]:
        res = []
        sentence_count = sum([len(p.sentences) for p in paragraphs])
        for index, paragraph in enumerate(paragraphs):
            paragraph_record = models.KnowledgeParagraph.create(**{
                "raw_content": "".join(paragraph.sentences),
                "index": index,
                "context_content": "".join(paragraph.sentences),
                "total_sentences": len(paragraph.sentences),
                "file": file
            })
            res.append(paragraph_record)

            for s_index, sentence in enumerate(paragraph.sentences):
                models.KnowledgeSentence.create(**{
                    "index": s_index,
                    "raw_content": sentence,
                    "vectorized": False,
                    "paragraph": paragraph_record,
                    "file": file
                })
        file.total_parts = sentence_count
        file.vectorized_parts = 0
        file.save(only=["total_parts", "vectorized_parts"])
        return res

    def get_paragraph_by_id(self, paragraph_id: int) -> Optional[models.KnowledgeParagraph]:
        return models.KnowledgeParagraph.get_or_none(paragraph_id)

    def list_messages_by_id_list(self, id_list: List[int]) -> Dict[int, models.MessageTab]:
        return {m.id: m for m in (
            models
            .MessageTab
            .select()
            .where(models.MessageTab.id.in_(id_list))
            .order_by(models.MessageTab.id.desc())
        )}

    def update_file_vectorized_count(self, file: models.KnowledgeBaseFileTab):
        file.vectorized_parts = models.KnowledgeSentence.select(peewee.fn.Count(peewee.SQL('1'))).where(
            models.KnowledgeSentence.file == file,
            models.KnowledgeSentence.vectorized == True
        ).scalar()
        file.save(only=["vectorized_parts"])

    def find_file_not_vectorized(self) -> Iterable[models.KnowledgeBaseFileTab]:
        return models.KnowledgeBaseFileTab.select().where(
            models.KnowledgeBaseFileTab.total_parts > 0,
            models.KnowledgeBaseFileTab.vectorized_parts == 0
        )

    def get_session_by_id(self, session_id: int) -> Optional[models.SessionTab]:
        return models.SessionTab.get_or_none(session_id)

    def get_msg_id(self, session_id: int) -> int:
        (models
         .SessionTab
         .update(**{
            "last_msg_id": models.SessionTab.last_msg_id + 1,
            "last_mst_ts": int(time.time())
        })
         .where(
            models.SessionTab.id == session_id
        )
         .execute())

        return list(
            models
            .SessionTab
            .select(
                models.SessionTab.last_msg_id
            )
            .where(
                models.SessionTab.id == session_id
            ).limit(1)
        )[0].last_msg_id

    def list_message_by_session_id(
            self, session: models.SessionTab, last_msg_id: int, limit: int = 20,
            action: GetHistoryType = GetHistoryType.BEFORE) -> Iterable[models.MessageTab]:
        if action == GetHistoryType.BEFORE:
            return (models.MessageTab.select()
                    .where(models.MessageTab.session == session, models.MessageTab.msg_id < last_msg_id)
                    .order_by(models.MessageTab.msg_id.desc()).limit(limit))
        return (models.MessageTab.select()
                .where(models.MessageTab.session == session, models.MessageTab.msg_id > last_msg_id)
                .order_by(models.MessageTab.msg_id).limit(limit))

    def get_last_message_by_session_id(self, session: models.SessionTab, limit: int = 10) -> List[models.MessageTab]:
        return list(models.MessageTab.select()
                    .where(models.MessageTab.session == session)
                    .order_by(models.MessageTab.msg_id.desc()).limit(limit))[::-1]

    def get_last_summarization_by_session_id(
            self, session: models.SessionTab, limit: int = 10) -> List[models.MessageSummarizationTab]:
        return list(models.MessageSummarizationTab.select()
                    .where(models.MessageSummarizationTab.session == session)
                    .order_by(models.MessageSummarizationTab.id.desc()).limit(limit))[::-1]

    def create_message_summarization(
            self, from_msg_id: int, to_msg_id: int, summarization: str, msg_count: int, session: models.SessionTab
    ) -> models.MessageSummarizationTab:
        return models.MessageSummarizationTab.create(**{
            "from_msg_id": from_msg_id,
            "to_msg_id": to_msg_id,
            "summarization": summarization,
            "msg_count": msg_count,
            "session": session
        })

    def create_ai_message(
            self,
            user: models.AuthUserTab,
            session: models.SessionTab,
            content: str,
            ai_msg_signature: str,
            question: Optional[models.MessageTab] = None
    ) -> models.MessageTab:
        ai_msg_id = self.get_msg_id(session.id)
        return models.MessageTab.create(**{
            "session": session,
            "msg_id": ai_msg_id,
            "role": ChatRole.assistant,
            "is_system": False,
            "client_ts": int(time.time()),
            "server_ts": int(time.time()),
            "is_answer": True,
            "question": question,
            "is_system_msg": False,
            "support_retry": True,
            "support_rating": True,
            "content": content,
            "text": "",
            "context_text": "",
            "version": 0,
            "user": user,
            "accepted": True,
            "msg_signature": ai_msg_signature,
            "rating": RatingType.NONE.value
        })

    def create_message_and_response(
            self,
            user: models.AuthUserTab,
            session: models.SessionTab,
            content: str,
            client_ts: int,
            ai_msg_signature: str,
            user_msg_signature: str
    ) -> Tuple[models.MessageTab, models.MessageTab]:
        user_msg_id = self.get_msg_id(session.id)
        log.info("user msg id = %s", user_msg_id)
        user_message = models.MessageTab.create(**{
            "session": session,
            "msg_id": user_msg_id,
            "role": ChatRole.user,
            "is_system": False,
            "client_ts": client_ts,
            "server_ts": int(time.time()),
            "is_answer": False,
            "is_system_msg": False,
            "support_retry": True,
            "support_rating": False,
            "content": CardMessage(components=[TextComponent(data=content)]).json(),
            "text": content,
            "context_text": content,
            "version": 0,
            "user": user,
            "msg_signature": user_msg_signature,
            "rating": RatingType.NONE.value
        })
        log.info("create user message: %s", model_to_dict(user_message))
        ai_message = self.create_ai_message(
            user, session, CardMessage(components=[]).json(), ai_msg_signature, user_message
        )
        return user_message, ai_message

    def get_message_by_msg_id(self, msg_id: int, session: models.SessionTab) -> Optional[models.MessageTab]:
        return models.MessageTab.get_or_none(msg_id=msg_id, session=session)

    def get_message_by_id(self, id_: int) -> Optional[models.MessageTab]:
        return models.MessageTab.get_or_none(id_)

    def update_message_content_text_context_text(
            self, msg_id: int, content: str, text: str, context_text: str, session: models.SessionTab) -> int:
        return (models.MessageTab.update(**{
            "content": content,
            "text": text,
            "context_text": context_text
        }).where(models.MessageTab.msg_id == msg_id, models.MessageTab.session == session).execute())

    def update_message_content(
            self, msg_id: int, content: str, session: models.SessionTab) -> int:
        return (models.MessageTab.update(**{"content": content})
                .where(models.MessageTab.msg_id == msg_id, models.MessageTab.session == session).execute())

    def update_message_rating(self, msg_id: int, rating: RatingType, session: models.SessionTab) -> int:
        return (models.MessageTab.update(**{"rating": rating})
                .where(models.MessageTab.msg_id == msg_id, models.MessageTab.session == session).execute())

    def update_message_support_retry(self, msg_id: int, support_retry: bool, session: models.SessionTab) -> int:
        return (models.MessageTab.update(**{"support_retry": support_retry})
                .where(models.MessageTab.msg_id == msg_id, models.MessageTab.session == session).execute())

    def set_vectorized(self, sentence_id: int, v: bool = True) -> int:
        return models.KnowledgeSentence.update(**{"vectorized": v}).where(
            models.KnowledgeSentence.id == sentence_id
        ).execute()

    def get_user_default_knowledgebase(self, user: models.AuthUserTab) -> models.KnowledgeBaseTab:
        return models.KnowledgeBaseTab.get_or_none(owner=user)

    def update_user_info(self, nickname: Optional[str], avatar: Optional[str], user: models.AuthUserTab) -> int:
        return (models.AuthUserTab.update(**{"nickname": nickname or user.nickname, "avatar": avatar or user.avatar})
                .where(models.AuthUserTab.id == user.id)).execute()

    def create_search_history(self, keyword: str, search_ts: int, user: models.AuthUserTab):
        models.SearchHistoryTab.create(**{
            "keyword": keyword,
            "search_ts": search_ts,
            "user": user
        })

    def list_search_history_by_user(
            self, user: models.AuthUserTab, include_empty: bool = True) -> Optional[List[models.SearchHistoryTab]]:
        query = models.SearchHistoryTab.select().where(models.SearchHistoryTab.user == user)
        if not include_empty:
            query = query.where(models.SearchHistoryTab.keyword != "")
        return list(query.execute())

    def get_xfconfig(self) -> models.XFConfig:
        return models.XFConfig.get_or_none()


class BusinessDataAccess:

    def get_data_by_cls_id(self, model_cls: Type[Model_T], id_: int, creator: models.AuthUserTab) -> Optional[Model_T]:
        conditions: List[bool] = [model_cls.id == id_, model_cls.creator == creator]
        if isinstance(model_cls, (models.SalaryTab, models.EmployeeLoanTab, models.ReceivablePayableTab)):
            conditions.append(getattr(model_cls, "write_off") == False)
        return model_cls.select().where(*conditions).first()

    def get_data_by_cls_id_dependencies(
            self, model_cls: Type[Model_T], id_: int, dep_fields: Dict[str, peewee.Model], creator: models.AuthUserTab
    ) -> Optional[Model_T]:
        if (model_cls is models.EmployeeTab) and dep_fields:
            employee = self.get_data_by_cls_id(models.EmployeeTab, id_, creator)
            conditions: List[bool] = [
                models.EmployeeProjectRecord.employee == employee,
                models.EmployeeProjectRecord.project == dep_fields["project"]
            ]
            if models.EmployeeProjectRecord.select().where(*conditions).first():
                return employee
            return None

        conditions: List[bool] = [model_cls.id == id_, model_cls.creator == creator]
        for field_name, field_value in dep_fields.items():
            conditions.append(getattr(model_cls, field_name) == field_value)
        if isinstance(model_cls, (models.SalaryTab, models.EmployeeLoanTab, models.ReceivablePayableTab)):
            conditions.append(getattr(model_cls, "write_off") == False)
        return model_cls.select().where(*conditions).first()

    def list_data_by_cls_creator(
            self, model_cls: Type[Model_T], creator: models.AuthUserTab, conditions: List[Any]
    ) -> Iterable[Model_T]:
        selector = model_cls.select()
        conditions: List[bool] = (conditions or []) + [model_cls.creator == creator]
        if isinstance(model_cls, (models.SalaryTab, models.EmployeeLoanTab, models.ReceivablePayableTab)):
            conditions.append(model_cls.write_off == False)
        if conditions:
            selector = selector.where(*conditions)
        return selector.execute()

    def update_account_amount_by_id(self, id_: int, amount: decimal.Decimal, creator: models.AuthUserTab) -> int:
        return (models.AccountTab
                .update(**{"amount": amount})
                .where(models.AccountTab.id == id_, models.AccountTab.creator == creator)
                .execute())

    def update_receivable_payable_completed_amount_write_off_by_id(
            self, id_: int, completed_amount: decimal.Decimal, write_off: bool, creator: models.AuthUserTab) -> int:
        return (models.ReceivablePayableTab
                .update(**{"completed_amount": completed_amount, "write_off": write_off})
                .where(models.ReceivablePayableTab.id == id_, models.ReceivablePayableTab.creator == creator)
                .execute())

    def update_employee_loan_completed_amount_by_id(
            self, id_: int, completed_amount: decimal.Decimal, creator: models.AuthUserTab) -> int:
        return (models.EmployeeLoanTab
                .update(**{"completed_amount": completed_amount})
                .where(models.EmployeeLoanTab.id == id_, models.EmployeeLoanTab.creator == creator)
                .execute())

    def update_employee_repayment_amount_write_off_by_id(
            self, id_: int, repayment_amount: decimal.Decimal, write_off: bool, creator: models.AuthUserTab) -> int:
        return (models.EmployeeLoanTab
                .update(**{"repayment_amount": repayment_amount, "write_off": write_off})
                .where(models.EmployeeLoanTab.id == id_, models.EmployeeLoanTab.creator == creator)
                .execute())

    def update_salary_completed_amount_write_off_by_id(
            self, id_: int, completed_amount: decimal.Decimal, write_off: bool, creator: models.AuthUserTab) -> int:
        return (models.SalaryTab
                .update(**{"completed_amount": completed_amount, "write_off": write_off})
                .where(models.SalaryTab.id == id_, models.SalaryTab.creator == creator)
                .execute())

    def update_contract_completed_amount_schedule_by_id(
            self, id_: int, completed_amount: decimal.Decimal, schedule: decimal.Decimal, creator: models.AuthUserTab
    ) -> int:
        return (models.ContractTab
                .update(**{"completed_amount": completed_amount, "schedule": schedule})
                .where(models.ContractTab.id == id_, models.ContractTab.creator == creator)
                .execute())

    def update_contract_invoice_amount_by_id(
            self, id_: int, total_amount: decimal.Decimal, creator: models.AuthUserTab) -> int:
        return (models.ContractTab
                .update(**{"invoice_total_amount": total_amount})
                .where(models.ContractTab.id == id_, models.ContractTab.creator == creator)
                .execute())

    def get_customer_by_name(self, name: str, creator: models.AuthUserTab) -> Optional[models.CustomerTab]:
        return models.CustomerTab.get_or_none(name=name, creator=creator)

    def get_supplier_by_name(self, name: str, creator: models.AuthUserTab) -> Optional[models.SupplierTab]:
        return models.SupplierTab.get_or_none(name=name, creator=creator)

    def get_account_by_name(self, name: str, creator: models.AuthUserTab) -> Optional[models.AccountTab]:
        return models.AccountTab.get_or_none(name=name, creator=creator)

    def get_employee_by_name(self, name: str, creator: models.AuthUserTab) -> Optional[models.EmployeeTab]:
        return models.EmployeeTab.get_or_none(name=name, creator=creator)

    def get_project_by_name(self, name: str, creator: models.AuthUserTab) -> Optional[models.ProjectTab]:
        return models.ProjectTab.get_or_none(name=name, creator=creator)

    def get_contract_by_number_name(
            self, number: str, name: str, creator: models.AuthUserTab) -> Optional[models.ContractTab]:
        return models.ContractTab.get_or_none(number=number, name=name, creator=creator)

    def get_invoice_by_number_code(
            self, number: str, code: str, creator: models.AuthUserTab) -> Optional[models.InvoiceTab]:
        return models.InvoiceTab.get_or_none(number=number, code=code, creator=creator)

    def get_salary_by_description(
            self, description: str, creator: models.AuthUserTab) -> Optional[models.SalaryTab]:
        return models.SalaryTab.get_or_none(description=description, creator=creator)

    def get_salary_by_date_name(
            self, date: str, employee: models.EmployeeTab, creator: models.AuthUserTab) -> Optional[models.SalaryTab]:
        year_month = re.search(r'(\d{4}年\d{1,2}月)', date).group(1)
        return (models.SalaryTab.select()
                .where(models.SalaryTab.date.startswith(year_month),
                       models.SalaryTab.employee == employee, models.SalaryTab.creator == creator).first())

    def get_employ_loan_by_date_name_description(
            self, date: str, employee: models.EmployeeTab, description: str, creator: models.AuthUserTab
    ) -> Optional[models.EmployeeLoanTab]:
        return (models.EmployeeLoanTab.select()
                .where(models.EmployeeLoanTab.date == date,
                       models.EmployeeLoanTab.employee == employee,
                       models.EmployeeLoanTab.description == description,
                       models.EmployeeLoanTab.creator == creator).first())

    def get_employee_loan_by_description(
            self, description: str, creator: models.AuthUserTab) -> Optional[models.EmployeeLoanTab]:
        return models.EmployeeLoanTab.get_or_none(description=description, creator=creator)

    def update_loan_adjust_amount_by_date_name_description(
            self, adjustment_amount: decimal.Decimal, date: str,
            employee: models.EmployeeTab, description: str, creator: models.AuthUserTab
    ) -> int:
        return (
            models.EmployeeLoanTab.update(**{"adjustment_amount": adjustment_amount})
            .where(models.EmployeeLoanTab.date == date,
                   models.EmployeeLoanTab.employee == employee,
                   models.EmployeeLoanTab.description == description,
                   models.EmployeeLoanTab.creator == creator).execute())

    def get_receivable_payable_by_description(
            self, description: str, creator: models.AuthUserTab) -> Optional[models.ReceivablePayableTab]:
        return models.ReceivablePayableTab.get_or_none(description=description, creator=creator)

    def create_account(self, name: str, amount: decimal.Decimal, creator: models.AuthUserTab) -> models.AccountTab:
        return models.AccountTab.create(**{
            "name": name,
            "amount": amount,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

    def create_employee(
            self, name: str, age: int, gender: GenderType, creator: models.AuthUserTab) -> models.EmployeeTab:
        return models.EmployeeTab.create(**{
            "name": name,
            "age": age,
            "gender": gender,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

    def create_transaction_item(self, name: str, creator: models.AuthUserTab) -> models.TransactionItemTab:
        return models.TransactionItemTab.create(**{
            "name": name,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

    def get_transaction_item_by_name(
            self, name: str, creator: models.AuthUserTab) -> Optional[models.TransactionItemTab]:
        try:
            return models.TransactionItemTab.get_or_none(name=name, creator=creator)
        except:
            return models.TransactionItemTab(id=0)

    def create_supplier(
            self, name: str, contact_name: str, contact_phone: str, creator: models.AuthUserTab) -> models.SupplierTab:
        return models.SupplierTab.create(**{
            "name": name,
            "contact_name": contact_name,
            "contact_phone": contact_phone,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

    def create_customer(
            self, name: str, contact_name: str, contact_phone: str, creator: models.AuthUserTab) -> models.CustomerTab:
        return models.CustomerTab.create(**{
            "name": name,
            "contact_name": contact_name,
            "contact_phone": contact_phone,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

    def create_project(
            self, name: str, start_date: str, end_date: str, budget: decimal.Decimal, creator: models.AuthUserTab
    ) -> models.ProjectTab:
        return models.ProjectTab.create(**{
            "name": name,
            "budget": budget,
            "start_date": start_date,
            "end_date": end_date,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "creator": creator
        })

    def create_employee_project_record(
            self, is_leader: bool, project: models.ProjectTab, employee: models.EmployeeTab
    ) -> models.EmployeeProjectRecord:
        return models.EmployeeProjectRecord.create(**{
            "is_leader": is_leader,
            "project": project,
            "employee": employee
        })

    def create_internal_transfer_record(
            self,
            source_account: models.AccountTab,
            target_account: models.AccountTab,
            amount: decimal.Decimal, description: str, date: str, creator: models.AuthUserTab
    ) -> models.InternalTransferTab:
        return models.InternalTransferTab.create(**{
            "amount": amount,
            "description": description,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "timestamp": int(datetime.strptime(date, '%Y年%m月%d日').timestamp()),
            "date": date,
            "target_account": target_account,
            "source_account": source_account,
            "creator": creator
        })

    def create_contract(
            self, contract: ContractInfo, project: models.ProjectTab,
            customer: Optional[models.CustomerTab], supplier: Optional[models.SupplierTab], creator: models.AuthUserTab
    ) -> models.ContractTab:
        return models.ContractTab.create(**{
            "number": contract.number,
            "name": contract.name,
            "type": contract.type,
            "amount": contract.amount,
            "adjustment_amount": contract.adjustment_amount,
            "start_date": contract.start_date,
            "end_date": contract.end_date,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "total_amount": contract.amount + contract.adjustment_amount,
            "completed_amount": decimal.Decimal(0),
            "schedule": decimal.Decimal(0),
            "invoice_total_amount": decimal.Decimal(0),
            "notes": contract.notes,
            "timestamp": int(datetime.strptime(contract.date, '%Y年%m月%d日').timestamp()),
            "date": contract.date,
            "project": project,
            "customer": customer,
            "supplier": supplier,
            "creator": creator
        })

    def create_invoice(
            self, invoice: InvoiceInfo, contract: models.ContractTab, creator: models.AuthUserTab
    ) -> models.InvoiceTab:
        return models.InvoiceTab.create(**{
            "amount": invoice.amount,
            "tax_rate": invoice.tax_rate,
            "type": invoice.type,
            "number": invoice.number,
            "code": invoice.code,
            "content": invoice.content,
            "notes": invoice.notes,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "no_tax_amount": invoice.amount / (1 + invoice.tax_rate),
            "tax_value": invoice.amount / (1 + invoice.tax_rate) * invoice.tax_rate,
            "submit_date": invoice.submit_date,
            "timestamp": int(datetime.strptime(invoice.date, '%Y年%m月%d日').timestamp()),
            "date": invoice.date,
            "contract": contract,
            "creator": creator
        })

    def create_employee_salary(
            self, salary: SalaryBill, employee: models.EmployeeTab, creator: models.AuthUserTab
    ) -> models.SalaryTab:
        payable_amount = salary.basic_salary + salary.overtime_pay + salary.attendance_bonus + salary.subsidy + salary.bonus
        deductible_amount = salary.leave_deduction + salary.other_deductions
        rates = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
        deductions = [0, 210, 1410, 2660, 4410, 7160, 15160]
        personal_tax = round(max(
            [(payable_amount - decimal.Decimal(5000)) * decimal.Decimal(rate) - decimal.Decimal(deduction)
             for rate, deduction in zip(rates, deductions)] + [decimal.Decimal('0')]), 2)
        net_salary = max(payable_amount - deductible_amount - personal_tax, decimal.Decimal("0"))
        return models.SalaryTab.create(**{
            "description": salary.description,
            "attendance_days": salary.attendance_days,
            "basic_salary": salary.basic_salary,
            "overtime_pay": salary.overtime_pay,
            "attendance_bonus": salary.attendance_bonus,
            "subsidy": salary.subsidy,
            "bonus": salary.bonus,
            "leave_deduction": salary.leave_deduction,
            "other_deductions": salary.other_deductions,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "payable_amount": payable_amount,
            "deductible_amount": deductible_amount,
            "personal_tax": personal_tax,
            "net_salary": net_salary,
            "completed_amount": decimal.Decimal(0),
            "write_off": False,
            "start_date": salary.start_date,
            "end_date": salary.end_date,
            "timestamp": int(datetime.strptime(salary.date, '%Y年%m月%d日').timestamp()),
            "date": salary.date,
            "employee": employee,
            "creator": creator
        })

    def create_employee_loan(
            self, loan_bill: LoanBill, employee: models.EmployeeTab, creator: models.AuthUserTab
    ) -> models.EmployeeLoanTab:
        return models.EmployeeLoanTab.create(**{
            "description": loan_bill.description,
            "amount": loan_bill.amount,
            "adjustment_amount": loan_bill.adjustment_amount,
            "repayment_amount": decimal.Decimal("0"),
            "offset_count": decimal.Decimal("0"),
            "completed_amount": decimal.Decimal("0"),
            "write_off": False,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "start_date": loan_bill.start_date,
            "end_date": loan_bill.end_date,
            "timestamp": int(datetime.strptime(loan_bill.date, '%Y年%m月%d日').timestamp()),
            "date": loan_bill.date,
            "employee": employee,
            "creator": creator
        })

    def create_transaction(
            self, t_record: TransactionRecord,
            account: models.AccountTab,
            transaction_item: models.TransactionItemTab,
            project: models.ProjectTab,
            receivable_payable: Optional[models.ReceivablePayableTab],
            salary: Optional[models.SalaryTab],
            employee_loan: Optional[models.EmployeeLoanTab], creator: models.AuthUserTab
    ) -> models.TransactionTab:
        transaction_data = {
            "voucher_number": t_record.voucher_number,
            "type": t_record.type,
            "description": t_record.description,
            "amount": t_record.amount,
            "account_remain_amount": account.amount,
            "notes": t_record.notes,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "date": t_record.date,
            "timestamp": int(datetime.strptime(t_record.date, '%Y年%m月%d日').timestamp()),
            "account": account,
            "transaction_item": transaction_item,
            "project": project,
            "creator": creator
        }
        log.info(f"这个交易数据是{transaction_data}")
        if receivable_payable:
            transaction_data["receivable_payable"] = receivable_payable
            if receivable_payable.contract:
                transaction_data["contract"] = receivable_payable.contract
        if salary:
            transaction_data["salary"] = salary
        if employee_loan:
            transaction_data["employee_loan"] = employee_loan
        log.info(f"这个交易数据是{transaction_data}")
        return models.TransactionTab.create(**transaction_data)

    def create_receivable_payable(
            self, receivable_payable_bill: ReceivablePayableBill, project: models.ProjectTab,
            employee: models.EmployeeTab, contract: Optional[models.ContractTab], creator: models.AuthUserTab
    ) -> models.ReceivablePayableTab:
        receivable_payable_data = {
            "description": receivable_payable_bill.description,
            "type": receivable_payable_bill.type,
            "amount": receivable_payable_bill.quantity * receivable_payable_bill.unit_price,
            "completed_amount": decimal.Decimal("0"),
            "write_off": False,
            "notes": receivable_payable_bill.notes,
            "create_date": datetime.fromtimestamp(int(time.time())).strftime('%Y年%m月%d日'),
            "create_at": int(time.time()),
            "start_date": receivable_payable_bill.start_date,
            "end_date": receivable_payable_bill.end_date,
            "date": receivable_payable_bill.date,
            "timestamp": int(datetime.strptime(receivable_payable_bill.date, '%Y年%m月%d日').timestamp()),
            "product_name": receivable_payable_bill.product_name,
            "specification": receivable_payable_bill.specification,
            "quantity": receivable_payable_bill.quantity,
            "unit_price": receivable_payable_bill.unit_price,
            "creator": creator,
            "project": project,
            "employee": employee
        }
        if contract:
            receivable_payable_data["contract"] = contract
        return models.ReceivablePayableTab.create(**receivable_payable_data)

    def get_project_transaction_amount_sum(
            self, project: models.ProjectTab, type_: TransactionType
    ) -> int:
        return models.TransactionTab.select(
            peewee.fn.Sum(models.TransactionTab.amount)
        ).where(
            models.TransactionTab.project == project,
            models.TransactionTab.type == type_
        ).scalar() or 0

    def get_project_members(self, project: models.ProjectTab) -> List[models.EmployeeTab]:
        return [record.employee for record in project.employee_project_record]

    # def select_employees(self, conditions: List[Any], user: models.AuthUserTab) -> Iterable[models.EmployeeTab]:
    #     log.info("[SelectEmployees] conditions: %s user: %s", conditions, user)
    #     selector = models.EmployeeTab.select()
    #     conditions = (conditions or []) + [models.EmployeeTab.creator == user]
    #     if conditions:
    #         selector = selector.where(*conditions)
    #     return selector

    def count_payable_receivable_bills_by_project_and_status(
            self, project: models.ProjectTab, user: models.AuthUserTab, type_: ReceivablePayableType,
            write_off: Optional[bool] = None
    ) -> int:
        conditions = [
            models.ReceivablePayableTab.project == project,
            models.ReceivablePayableTab.creator == user,
            models.ReceivablePayableTab.type == type_,
        ]
        if write_off is not None:
            conditions.append(models.ReceivablePayableTab.write_off == write_off)

        return models.ReceivablePayableTab.select(
            peewee.fn.Count(peewee.SQL('1'))
        ).where(
            *conditions
        ).scalar()


data_access = DataAccess()
business_data_access = BusinessDataAccess()
