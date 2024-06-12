from fastapi import Request
from app.utils.logger import logger
from typing import Callable

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