from app.models.user import User as UserModel
from fastapi.responses import JSONResponse
from app.utils.logger import logger
from fastapi import Depends, HTTPException, Request,status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.auth import decode_access_token
from app.utils.logger import logger
from app.repository.user_repository import UserRepository
from app.service.user_service import UserService
from app.service.auth_service import AuthService
from typing import List, Union
from app.schemas.response import ErrorResponse
#from app.core.handlers.http_handlers import http_exception_handler


# UserRepository 의존성 주입을 위한 함수
def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    logger.info('get_user_repository 함수 호출됨')
    return UserRepository(db)

def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repository)

# UserService 의존성 주입을 위한 함수
def get_user_service(user_repository: UserRepository = Depends(get_user_repository)) -> UserService:
    logger.info('get_user_service 함수 호출됨')
    return UserService(user_repository)

# === 예외 ==========================================
# 예외 핸들러 가져오기 함수
##def get_http_exception_handler():
##    logger.info('get_http_exception_handler 함수 호출됨')
#    return http_exception_handler


# === JWT =========================================
# 현재 사용자 가져오기 함수

async def get_current_user(request: Request, db: Session = Depends(get_db)) -> UserModel:
    logger.info('get_current_user 함수 호출됨')
    
    # JWT 쿠키가 존재하지 않는 경우 예외
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT가 존재하지 않습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    logger.warn(f'쿠키에서 가져온 토큰: {token}')
    
    # JWT 디코딩 시 예외 발생 시 처리
    try:
        payload = decode_access_token(token)
    except HTTPException as e:
        if e.detail == "Token has expired":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="JWT가 만료되었습니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="유효하지 않은 JWT입니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    # 디코딩 후 payload가 None인 경우 예외
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT 디코딩에 실패했습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    email: str = payload.get("sub")
    
    # JWT에 이메일 정보가 없는 경우 예외
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="JWT에 유효한 이메일 정보가 없습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = db.query(UserModel).filter(UserModel.email == email).first()
    
    # 이메일에 해당하는 사용자를 찾을 수 없는 경우 예외
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 이메일로 사용자를 찾을 수 없습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    logger.info(f"사용자 확인됨: {user.email}")
    return user