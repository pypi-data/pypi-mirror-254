import inspect
import sys
from rmbcommon.exceptions.server import *

class ServerConnectionError(Exception):
    code = 9002
    message = "Server Connection Error"


class ServerUnknownError(Exception):
    code = 9003
    message = "Server Unknown Error"


def get_exception_by_code(code):
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if getattr(obj, 'code') == code:
                return obj
    return None


def raise_exception_by_code(code, message):
    ex = get_exception_by_code(code)
    if ex:
        raise ex(message)
    else:
        raise ServerUnknownError(f"Unknown error code: {code} {message}")
