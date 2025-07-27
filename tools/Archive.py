from enum import Enum
import json

class ArchiveExt(Enum):
    TAR = 'tar'
    TAR_GZ = 'tar.gz'
    TAR_XZ = 'tar.xz'
    ZIP = 'zip'
    BZ2 = 'bz2'

    def __str__(self):
        return self.value

class Archive:
# url
# filename
# path
# sha1
# sha256
# md5
# ext
#     - tar
#     - tar.gz
#     - tar.xz
#     - zip
    def __init__(self, url: str, filename: str, path: str, ext:ArchiveExt, sha1: str = None, sha256: str = None, md5: str = None):
        self.url = url
        self.filename = filename
        self.path = path
        self.ext = ext
        self.sha1 = sha1
        self.sha256 = sha256
        self.md5 = md5

    def __str__(self):
        return f"Archive(url={self.url}, filename={self.filename}, path={self.path}, ext={self.ext} sha1={self.sha1}, sha256={self.sha256}, md5={self.md5})"

    @classmethod
    def from_json(cls, data):
        _archive = cls(data.get('url'),data.get('filename'),data.get('path'),ArchiveExt(data.get('ext')))

        if 'md5' in data:
            _archive.md5 = data.get('md5')

        if 'sha1' in data:
            _archive.sha1 = data.get('sha1')

        if 'sha256' in data:
            _archive.sha256 = data.get('sha256')

        return _archive


    def to_json(self):
        _json = {
            'url': self.url,
            'filename': self.filename,
            'path': self.path,
            'ext': str(self.ext)
        }
        if self.sha1:
            _json['sha1'] = self.sha1
        if self.sha256:
            _json['sha256'] = self.sha256
        if self.md5:
            _json['md5'] = self.md5
        return _json

    def to_json_str(self):
        return json.dumps(self.to_json(), indent=4)

    @staticmethod
    def from_json_str(json_str):
        try:
            data = json.loads(json_str)
            return Archive.from_json(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON string: {e}")
