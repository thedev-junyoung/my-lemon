from pydantic import BaseModel, Field
from typing import Any, List, Optional, Union

class SuccessResponse(BaseModel):
    status: str = "success"
    data: Any = None  # 실제 데이터를 포함
    message: Optional[str] = "요청이 성공적으로 처리되었습니다."

class ErrorDetail(BaseModel):
    loc: List[str]
    msg: str
    type: str

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
    errors: Optional[Union[List[ErrorDetail], str]] = None
