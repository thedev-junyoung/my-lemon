from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.user import UserCreate, UserLogin
from app.schemas.auth import TokenRefreshRequest
from app.schemas.response import SuccessResponse
from app.models.user import User as UserModel
from app.core.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_user_refresh_token,
    generate_csrf_token
)
from app.db.session import get_db
from app.core.dependencies import get_http_exception_handler
from app.models.refresh_token import RefreshToken
from app.core.config import settings
from app.utils.logger import logger

router = APIRouter()

# === 공통 함수 ============================================================================
def set_response_cookie(response: Response, access_token: str):
    response.set_cookie(
        key="access_token",
        value=access_token,
        secure=settings.SECURE_COOKIES,
        samesite=settings.SAMESITE_POLICY,
        httponly=settings.HTTPONLY_COOKIES,
    )

# === 회원가입 API =========================================================================
@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    hashed_password = get_password_hash(user.password)
    new_user = UserModel(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return SuccessResponse(message="회원가입 완료", data={"id": new_user.id, "name": new_user.name, "email": new_user.email})

# === 로그인 API ===========================================================================
@router.post("/login", response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="이메일 또는 비밀번호가 잘못되었습니다.")
    
    # 토큰 생성
    access_token = create_access_token(data={"sub": db_user.email})
    csrf_token = generate_csrf_token()
    create_refresh_token(db_user.id, db)
    
    # JWT를 HTTP Only 쿠키로 설정
    set_response_cookie(response, access_token)

    logger.info("Login successful for user: %s", user.email)
    
    # 응답 헤더에 CSRF 토큰 포함
    response.headers["X-CSRF-Token"] = csrf_token
    
    return SuccessResponse()

# === 리프레시 토큰 재발급 API ==============================================================
@router.post("/refresh-token", response_model=SuccessResponse)
async def refresh_access_token(token_data: TokenRefreshRequest, response: Response, db: Session = Depends(get_db)):
    user = verify_user_refresh_token(token_data.id, db)
    if not user:
        raise HTTPException(status_code=401, detail="유효하지 않거나 만료된 리프레시 토큰입니다.")
    
    access_token = create_access_token(data={"sub": user.email})
    
    # JWT를 HTTP Only 쿠키로 설정
    set_response_cookie(response, access_token)
    
    return SuccessResponse(message="토큰이 성공적으로 갱신되었습니다.")

# === 로그아웃 API ==========================================================================
@router.post("/logout", response_model=SuccessResponse)
async def logout(token_data: TokenRefreshRequest, response: Response, db: Session = Depends(get_db)):
    refresh_token = db.query(RefreshToken).filter(
        RefreshToken.user_id == token_data.id,
        RefreshToken.expires_at >= datetime.now(timezone.utc)
    ).first()
    
    if refresh_token:
        db.delete(refresh_token)
        db.commit()
    
    # JWT를 삭제하기 위해 쿠키 제거
    response.delete_cookie(
        key="access_token",
        httponly=settings.HTTPONLY_COOKIES,
        secure=settings.SECURE_COOKIES,
        samesite=settings.SAMESITE_POLICY
    )
    
    return SuccessResponse(message="로그아웃 완료")

# === CSRF 토큰 생성 API 추가 ===============================================================
@router.get("/csrf-token", response_model=SuccessResponse)
def get_csrf_token(response: Response):
    csrf_token = generate_csrf_token()
    response.headers["X-CSRF-Token"] = csrf_token
    return SuccessResponse(message="CSRF token generated", data={"csrf_token": csrf_token})

