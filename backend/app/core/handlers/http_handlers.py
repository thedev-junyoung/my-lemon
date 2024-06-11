# app/core/handlers/http_handlers.py

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.schemas.response import ErrorResponse, ErrorDetail
from typing import Union, List

async def http_exception_handler(request: Request, exc: Union[HTTPException, RequestValidationError]):
    if isinstance(exc, HTTPException):
        if exc.status_code == 401:
            message = "인증이 필요합니다."
        elif exc.status_code == 402:
            message = "결제가 필요합니다."
        elif exc.status_code == 403:
            message = "접근이 금지되었습니다."
        elif exc.status_code == 404:
            message = "요청한 리소스를 찾을 수 없습니다."
        elif exc.status_code == 429:
            message = "요청이 너무 많습니다. 잠시 후 다시 시도해 주세요."
        else:
            message = str(exc.detail)

        response_content = ErrorResponse(
            status="error",
            code=0,
            message=message,
            errors=str(exc.status_code)
        )
        return JSONResponse(status_code=exc.status_code, content=response_content.model_dump())

    elif isinstance(exc, RequestValidationError):
        errors: List[ErrorDetail] = [
            ErrorDetail(loc=".".join(map(str, err["loc"])), msg=err["msg"], type=err["type"]) for err in exc.errors()
        ]
        response_content = ErrorResponse(
            status="error",
            code=0,
            message="유효하지 않은 요청입니다.",
            errors=errors
        )
        return JSONResponse(status_code=422, content=response_content.model_dump())
    else:
        response_content = ErrorResponse(
            status="error",
            code=0,
            message="서버에 오류가 발생했습니다.",
            errors=str(exc)
        )
    return JSONResponse(status_code=500, content=response_content.model_dump_json())
