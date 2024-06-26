# app/core/auth.py

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from typing import Union, Dict
import jwt
import os
from passlib.context import CryptContext
from app.db.session import get_db
from app.models.user import User as UserModel
from app.models.refresh_token import RefreshToken
import secrets
import hmac
from app.utils.logger import logger
from app.core.exceptions import JWTTokenMissingException, JWTTokenExpiredException, JWTTokenInvalidException, UserNotFoundException

# OAuth2 설정
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# 환경 변수에서 키를 가져옴
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# 비밀번호 해시화 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해시화 함수
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 비밀번호 검증 함수
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# === JWT ===========================================================================
# JWT 토큰 생성 함수
def create_access_token(data: dict, expires_delta: timedelta = None):
    logger.info('')
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# JWT 토큰 디코딩 함수
def decode_access_token(token: str) -> Union[Dict[str, Union[str, int]], None]:
    logger.info('')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# JWT 토큰 검증 함수
def verify_jwt_token(token: str) -> Dict[str, Union[str, int]]:
    logger.info(f'token:{token}')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

# 현재 사용자 가져오기 함수
async def get_current_user(request: Request, db: Session = Depends(get_db)) -> UserModel:
    logger.info('get_current_user 함수 호출됨')
    
    token = request.cookies.get("access_token")
    if not token:
        logger.error("JWT가 존재하지 않습니다.")
        raise JWTTokenMissingException()

    logger.warn(f'쿠키에서 가져온 토큰: {token}')
    
    try:
        payload = decode_access_token(token)
    except HTTPException as e:
        if e.detail == "Token has expired":
            logger.error("JWT가 만료되었습니다.")
            raise JWTTokenExpiredException()
        else:
            logger.error("유효하지 않은 JWT입니다.")
            raise JWTTokenInvalidException()

    if payload is None:
        logger.error("JWT 디코딩에 실패했습니다.")
        raise JWTTokenInvalidException()

    email: str = payload.get("sub")
    
    if email is None:
        logger.error("JWT에 유효한 이메일 정보가 없습니다.")
        raise JWTTokenInvalidException()

    user = db.query(UserModel).filter(UserModel.email == email).first()
    
    if user is None:
        logger.error(f"해당 이메일로 사용자를 찾을 수 없습니다: {email}")
        raise UserNotFoundException(email)
    
    logger.info(f"사용자 확인됨: {user.email}")
    return user

# 현재 활성 사용자 가져오기 함수
async def get_current_active_user(current_user: UserModel = Depends(get_current_user)) -> UserModel:
    logger.info('get_current_active_user()')
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user

def create_refresh_token(user_id: int, db: Session):
    logger.info('create_refresh_token()')
    token = secrets.token_urlsafe(64)
    expires_at = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = RefreshToken(
        user_id=user_id,
        token=token,
        expires_at=expires_at
    )
    db.add(refresh_token)
    db.commit()
    return token

def verify_refresh_token(token: str, db: Session):
    refresh_token = db.query(RefreshToken).filter(RefreshToken.token == token).first()
    if not refresh_token or refresh_token.expires_at < datetime.now(timezone.utc):
        return None
    return refresh_token.user_id

def verify_user_refresh_token(user_id: int, db: Session):
    """
    사용자 ID를 통해 리프레시 토큰의 유효성을 확인합니다.
    """
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return None

    refresh_token = db.query(RefreshToken).filter(
        RefreshToken.user_id == user.id,
        RefreshToken.expires_at >= datetime.now(timezone.utc)
    ).first()

    if not refresh_token:
        return None

    return user  # 유효한 리프레시 토큰이 있는 경우 사용자 반환

# === CSP =====================================================================================

CSRF_SECRET_KEY = "your-very-secure-csrf-secret-key"
CSRF_TOKEN_TIMEOUT = 3600  # 1 hourCSRF_TOKEN_TIMEOUT = 3600  # 1 hour

# === CSRF =====================================================================================
def generate_csrf_token() -> str:
    logger.info('generate_csrf_token()')
    expiration_time = (datetime.now(timezone.utc) + timedelta(seconds=CSRF_TOKEN_TIMEOUT)).timestamp()
    data = f"{expiration_time}"
    token = hmac.new(CSRF_SECRET_KEY.encode(), data.encode(), digestmod='sha256').hexdigest()
    return f"{token}:{expiration_time}"

def validate_csrf_token(csrf_token: str) -> bool:
    logger.info('validate_csrf_token()')
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

# === 테스트용 인증 헤더 생성 함수 ===========================================================
# 테스트용 인증 헤더 생성 함수
def get_auth_headers(user_email: str) -> dict:
    """테스트용 JWT 및 CSRF 토큰을 생성하여 인증 헤더를 반환합니다."""
    jwt_token = create_access_token(data={"sub": user_email}, expires_delta=timedelta(minutes=60))
    csrf_token = generate_csrf_token()
    return {
        "Authorization": f"Bearer {jwt_token}",
        "X-CSRF-Token": csrf_token
    }