# Stubs for requests.packages.urllib3.response (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, IO
import io
from . import _collections
from . import exceptions
# from .packages import six
from . import connection
from .util import response

HTTPHeaderDict = _collections.HTTPHeaderDict
ProtocolError = exceptions.ProtocolError
DecodeError = exceptions.DecodeError
ReadTimeoutError = exceptions.ReadTimeoutError
binary_type = str  # six.binary_type
PY3 = True  # six.PY3
is_fp_closed = response.is_fp_closed

class DeflateDecoder:
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def decompress(self, data): ...

class GzipDecoder:
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def decompress(self, data): ...

class HTTPResponse(IO[Any]):
    CONTENT_DECODERS = ...  # type: Any
    REDIRECT_STATUSES = ...  # type: Any
    headers = ...  # type: Any
    status = ...  # type: Any
    version = ...  # type: Any
    reason = ...  # type: Any
    strict = ...  # type: Any
    decode_content = ...  # type: Any
    def __init__(self, body=..., headers=..., status=..., version=..., reason=..., strict=..., preload_content=..., decode_content=..., original_response=..., pool=..., connection=...) -> None: ...
    def get_redirect_location(self): ...
    def release_conn(self): ...
    @property
    def data(self): ...
    def tell(self): ...
    def read(self, amt=..., decode_content=..., cache_content=...): ...
    def stream(self, amt=..., decode_content=...): ...
    @classmethod
    def from_httplib(ResponseCls, r, **response_kw): ...
    def getheaders(self): ...
    def getheader(self, name, default=...): ...
    def close(self): ...
    @property
    def closed(self): ...
    def fileno(self): ...
    def flush(self): ...
    def readable(self): ...
    def readinto(self, b): ...
