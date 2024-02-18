import abc
import io
import re
from enum import Enum
from typing import List, Optional, Union

import pdfplumber
import pydocx
from pydantic import BaseModel


class FileExtension(str, Enum):
    doc = "doc"
    docx = "docx"
    pdf = "pdf"
    txt = "txt"

    @classmethod
    def _missing_(cls, value: str) -> 'FileExtension':
        value = value.lower()
        return FileExtension(value)


class Paragraph(BaseModel):
    index: int = 0
    sentences: List[str] = []


class ContentExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_content(self, file_path: Union[str, io.IOBase]) -> List[Paragraph]:
        pass


def split_text(document: str) -> List[str]:
    delimiter_pattern = r'([\n。！？.!?])'
    segments = re.split(delimiter_pattern, document)
    sentences = [segments[i] + segments[i + 1] for i in range(0, len(segments) - 1, 2)]
    if len(segments) % 2 == 1:
        sentences.append(segments[-1])
    return sentences

class EmptyFile(Exception):
    def __init__(self, message):
        self.message = message

class TxtExtractor(ContentExtractor):
    paragraph_threshold = 300  # paragraph 必须是有换行分割、符号分割
    sentence_threshold = 30

    def extract_content(self, file_path: Union[str, io.StringIO]) -> List[Paragraph]:
        if isinstance(file_path, io.IOBase):
            content = file_path.read()
        else:
            with open(file_path, "r") as f:
                content = f.read()
        res: List[Paragraph] = []
        current_paragraph: Optional[Paragraph] = None

        for sentence in split_text(content):
            if not current_paragraph or len("".join(current_paragraph.sentences)) >= self.paragraph_threshold:
                current_paragraph = Paragraph()
                res.append(current_paragraph)
            current_paragraph.sentences.append(sentence)
        for p in res:
            p.sentences = [s for s in p.sentences if s.strip()]
        return res


class DocExtractor(ContentExtractor):
    paragraph_threshold = 300  # paragraph 必须是有换行分割、符号分割
    sentence_threshold = 30

    def extract_content(self, file_path: str) -> List[Paragraph]:
        markdown = pydocx.PyDocX.to_markdown(file_path)
        text = "\n".join(map(str, markdown))
        return TxtExtractor().extract_content(io.StringIO(text))


class PDFExtractor(ContentExtractor):
    def extract_content(self, file_path: Union[str, io.IOBase]) -> List[Paragraph]:
        lines = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                for line in page.extract_text_simple().splitlines():
                    if len(line) <= 1:
                        continue
                    lines.append(line)
        text = "\n".join(lines)
        if not text:
            raise EmptyFile("file is empty")
        return TxtExtractor().extract_content(io.StringIO(text))

def get_extractor(extension: str) -> ContentExtractor:
    if extension == "pdf":
        return PDFExtractor()
    if extension in {"doc", "docx"}:
        return DocExtractor()
    if extension in {"txt"}:
        return TxtExtractor()


def test_txt_extractor():
    a = TxtExtractor().extract_content("/home/lajunkai/Desktop/abc.txt")
    print(a)


def test_docx_extractor():
    a = DocExtractor().extract_content(
        "/home/lajunkai/PycharmProjects/lemon-rag/lemon_rag/llm/agents/rag/城镇燃气经营安全重大隐患判定标准.docx"
    )
    print(a)


def test_pdf_extractor():
    a = PDFExtractor().extract_content(
        "/home/lajunkai/Downloads/建筑装饰装修工程质量验收标准.pdf"
    )
    print(a)
