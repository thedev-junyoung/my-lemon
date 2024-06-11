# app/core/security.py
from fastapi import Request, HTTPException, Response
from datetime import datetime, timedelta, timezone
from typing import Callable
import secrets
from app.utils.logger import logger
import hmac

CSRF_SECRET_KEY = "your-very-secure-csrf-secret-key"
CSRF_TOKEN_TIMEOUT = 3600  # 1 hourCSRF_TOKEN_TIMEOUT = 3600  # 1 hour

# Content Security Policy (CSP) 미들웨어
async def csp_middleware(request: Request, call_next: Callable):
    logger.info('')
    # 먼저 요청을 다음 미들웨어 또는 엔드포인트로 전달합니다.
    response = await call_next(request)  # 비동기적으로 다음 요청 처리
    
    csp_dev = "default-src 'self' data: 'unsafe-inline' 'unsafe-eval' https://*; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*; img-src 'self' data: https://*;"
    csp_prod = "default-src 'self'; script-src 'self'; img-src 'self' data:;"
    
    environment = "development"
    csp_header = csp_dev if environment == "development" else csp_prod
    
    # 응답 헤더에 CSP 설정을 추가합니다.
    response.headers["Content-Security-Policy"] = csp_header
    return response


def generate_csrf_token() -> str:
    expiration_time = (datetime.now(timezone.utc) + timedelta(seconds=CSRF_TOKEN_TIMEOUT)).timestamp()
    data = f"{expiration_time}"
    token = hmac.new(CSRF_SECRET_KEY.encode(), data.encode(), digestmod='sha256').hexdigest()
    return f"{token}:{expiration_time}"

def validate_csrf_token(csrf_token: str) -> bool:
    if not csrf_token:
        raise HTTPException(status_code=403, detail="CSRF token not found")
    
    try:
        token, exp_time = csrf_token.split(':')
        exp_time = float(exp_time)
    except ValueError:
        raise HTTPException(status_code=403, detail="Invalid CSRF token format")
    
    if datetime.now(timezone.utc).timestamp() > exp_time:
        raise HTTPException(status_code=403, detail="CSRF token expired")
    
    expected_token = hmac.new(CSRF_SECRET_KEY.encode(), f"{exp_time}".encode(), digestmod='sha256').hexdigest()
    
    if not hmac.compare_digest(expected_token, token):
        raise HTTPException(status_code=403, detail="CSRF token invalid")
    
    return True