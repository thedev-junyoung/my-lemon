# app/middleware/csrf.py
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.auth import validate_csrf_token
from app.utils.logger import logger
EXEMPT_PATHS = ["/auth/login", "/auth/signup"]  # CSRF 검증을 생략할 경로들

class CSRFMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info('')
        if request.method not in ["GET", "HEAD", "OPTIONS"] and not any(request.url.path.startswith(path) for path in EXEMPT_PATHS):
            csrf_token = request.headers.get("X-CSRF-Token")
            if not csrf_token:
                raise HTTPException(status_code=403, detail="CSRF token is missing")
            validate_csrf_token(csrf_token)
        response = await call_next(request)
        logger.info(f'response:{response}')
        return response