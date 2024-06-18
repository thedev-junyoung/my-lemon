# response.py
from pydantic import BaseModel, Field
from typing import Any, Optional, Dict

class ErrorResponse(BaseModel):
    statusCode: int
    errorMessage: str
    errorDetails: Dict[str, Any] = Field(default_factory=dict)

class SuccessResponse(BaseModel):
    status: str = "success"
    code: int = 1
    data: Any = None  # 실제 데이터를 포함
    message: Optional[str] = "요청이 성공적으로 처리되었습니다."
    
    