from app.core.handlers.http_handlers import http_exception_handler
from app.core.auth import get_current_user, get_current_active_user
from fastapi import Depends
from app.models.user import User as UserModel
from app.core.auth import verify_jwt_token, oauth2_scheme


# === 예외 ==========================================
def get_http_exception_handler():
    return http_exception_handler

# === JWT =========================================
# JWT 인증을 통해 현재 사용자와 활성 사용자를 가져오는 함수들을 정의
async def get_active_user(current_user: UserModel = Depends(get_current_active_user)):
    return current_user

async def get_authenticated_user(current_user: UserModel = Depends(get_current_user)):
    return current_user

# 토큰 검증 함수
async def get_current_token(token: str = Depends(oauth2_scheme)):
    return verify_jwt_token(token)