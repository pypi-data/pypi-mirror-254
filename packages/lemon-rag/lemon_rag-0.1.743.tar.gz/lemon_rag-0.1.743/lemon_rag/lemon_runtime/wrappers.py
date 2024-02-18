from typing import Optional, List


class RuntimeFile:
    name: str
    status: bool
    body: bytes
    file_path: str
    url: str

    def save(self):
        pass

    def load(self):
        pass


class FileFieldValue:
    file_list: List[RuntimeFile]

    def add(self, file_obj: RuntimeFile):
        pass

    def get_by_name(self, name) -> RuntimeFile:
        pass

    def get_file_list(self):
        pass

    def add_file(self, body, name=None, file_path=None):
        # save and add
        pass


class FileSystem:
    def create_file(
            self,
            body: bytes,
            name: str,
            file_path: Optional[str] = None,
            url: Optional[str] = None
    ) -> RuntimeFile:
        pass

    def file_field(self, file_list: Optional[List[RuntimeFile]] = None):
        return FileFieldValue


class OSSBucket:
    def sign_url(self, path, method="GET", expires=600, slash_safe=True, headers=None) -> str:
        pass


class Utils:
    oss_bucket: OSSBucket


class Lemon:
    utils: Utils


file_system: FileSystem
lemon: Lemon
