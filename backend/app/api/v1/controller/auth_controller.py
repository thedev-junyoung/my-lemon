# app/api/v1/controller/auth_controller.py

from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.schemas.user import UserCreate, UserLogin
from app.schemas.auth import TokenRefreshRequest
from app.schemas.response import SuccessResponse
from app.service.auth_service import AuthService
from app.core.dependencies import get_auth_service
from app.utils.logger import logger
from app.core.config import settings
from app.core.auth import generate_csrf_token

class AuthController:
    def __init__(self):
        logger.info('AuthController 클래스 생성')


    async def create_user(self, user: UserCreate, auth_service: AuthService = Depends(get_auth_service)):
        try:
            new_user = auth_service.create_user(user)
            return SuccessResponse(
                message="회원가입 완료",
                data={"id": new_user.id, "name": new_user.name, "email": new_user.email}
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def login(self, user: UserLogin, response: Response, auth_service: AuthService = Depends(get_auth_service)):
        try:
            db_user = auth_service.authenticate_user(user)
            tokens = auth_service.create_tokens(db_user)
            response.set_cookie(
                key="access_token",
                value=tokens["access_token"],
                secure=settings.SECURE_COOKIES,
                samesite=settings.SAMESITE_POLICY,
                httponly=settings.HTTPONLY_COOKIES,
            )
            response.headers["X-CSRF-Token"] = tokens["csrf_token"]
            return SuccessResponse()
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def refresh_access_token(self, token_data: TokenRefreshRequest, response: Response, auth_service: AuthService = Depends(get_auth_service)):
        user = auth_service.verify_refresh_token(token_data.id)
        if not user:
            raise HTTPException(status_code=401, detail="유효하지 않거나 만료된 리프레시 토큰입니다.")
        tokens = auth_service.create_tokens(user)
        response.set_cookie(
            key="access_token",
            value=tokens["access_token"],
            secure=settings.SECURE_COOKIES,
            samesite=settings.SAMESITE_POLICY,
            httponly=settings.HTTPONLY_COOKIES,
        )
        return SuccessResponse(message="토큰이 성공적으로 갱신되었습니다.")

    async def logout(self, token_data: TokenRefreshRequest, response: Response, auth_service: AuthService = Depends(get_auth_service)):
        auth_service.delete_user_refresh_token(token_data.id)
        response.delete_cookie(
            key="access_token",
            httponly=settings.HTTPONLY_COOKIES,
            secure=settings.SECURE_COOKIES,
            samesite=settings.SAMESITE_POLICY
        )
        return SuccessResponse(message="로그아웃 완료")

    async def get_csrf_token(self, response: Response):
        csrf_token = generate_csrf_token()
        response.headers["X-CSRF-Token"] = csrf_token
        return SuccessResponse(message="CSRF token generated", data={"csrf_token": csrf_token})
