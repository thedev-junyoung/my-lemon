from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.user import UserCreate, UserLogin
from app.schemas.auth import TokenRefreshRequest
from app.schemas.response import SuccessResponse
from app.models.user import User as UserModel
from app.core.auth import get_password_hash, verify_password, create_access_token, decode_access_token, verify_refresh_token, create_refresh_token, verify_user_refresh_token
from app.db.session import get_db
from app.core.dependencies import get_http_exception_handler
from app.core.security import generate_csrf_token
from app.models.refresh_token import RefreshToken
router = APIRouter()

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

@router.post("/login", response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="이메일 또는 비밀번호가 잘못되었습니다.")
    # 토큰 생성
    access_token = create_access_token(data={"sub": db_user.email})
    csrf_token = generate_csrf_token()
    # 리프레시 토큰 생성 및 데이터베이스에 저장
    refresh_token = create_refresh_token(db_user.id, db)
    # 응답 헤더에 토큰 포함
    response.headers["Authorization"] = f"Bearer {access_token}"
    response.headers["X-CSRF-Token"] = csrf_token

    return SuccessResponse()

@router.post("/refresh-token", response_model=SuccessResponse)
async def refresh_access_token(token_data: TokenRefreshRequest, response: Response, db: Session = Depends(get_db)):
    """
    클라이언트로부터 사용자 ID를 받아 리프레시 토큰 테이블을 확인하고,
    유효한 경우 새로운 액세스 토큰을 발급합니다.
    """
    user = verify_user_refresh_token(token_data.id, db)
    if not user:
        raise HTTPException(status_code=401, detail="유효하지 않거나 만료된 리프레시 토큰입니다.")

    access_token = create_access_token(data={"sub": str(user.id)})
    response.headers["Authorization"] = f"Bearer {access_token}"

    return SuccessResponse(message="토큰이 성공적으로 갱신되었습니다.")

@router.post("/logout", response_model=SuccessResponse)
async def logout(token_data: TokenRefreshRequest, db: Session = Depends(get_db)):
    """
    로그아웃 시 리프레시 토큰을 폐기합니다.
    """
    refresh_token = db.query(RefreshToken).filter(
        RefreshToken.user_id == token_data.id,
        RefreshToken.expires_at >= datetime.now(timezone.utc)
    ).first()

    if refresh_token:
        db.delete(refresh_token)
        db.commit()

    return SuccessResponse(message="로그아웃 완료")


# CSRF 토큰 생성 API 추가
@router.get("/csrf-token", response_model=SuccessResponse)
def get_csrf_token(response: Response):
    csrf_token = generate_csrf_token()
    response.headers["X-CSRF-Token"] = csrf_token
    return SuccessResponse(message="CSRF token generated", data={"csrf_token": csrf_token})

