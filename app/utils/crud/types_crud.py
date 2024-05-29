from typing import Any, Generic, TypedDict, TypeVar


class ResponseMessage[T]( TypedDict, total=False):
    success_status: bool
    message: str
    error: Any
    data: T | None
    doc_length: int|None


def response_message[U](success_status: bool, message: str, error: Any|None=None, data: U | None=None, doc_length: int|None=None) -> ResponseMessage[U]:
    if success_status:
        return {
            "success_status": success_status,
            "message": message,
            "data": data,
            "doc_length": doc_length
        }
    else:
        return {
            "success_status": success_status,
            "message": message,
            "error": str(error),
            "doc_length": doc_length
        }
