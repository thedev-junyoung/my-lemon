# exception_handlers.py

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.core.exceptions import BaseAppException
from app.schemas.response import ErrorResponse

async def base_app_exception_handler(request: Request, exc: BaseAppException):
    error_response = ErrorResponse(
        statusCode=exc.status_code,
        errorMessage=exc.error_message,
        errorDetails={
            "path": request.url.path,
            "method": request.method
        }
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.dict()
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    error_response = ErrorResponse(
        statusCode=exc.status_code,
        errorMessage=exc.detail if isinstance(exc.detail, str) else "HTTP Exception",
        errorDetails={
            "path": request.url.path,
            "method": request.method
        }
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.dict()
    )
