from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.schemas.user import UserCreate, UserLogin, Token, User
from app.schemas.response import SuccessResponse, ErrorResponse
from app.models.user import User as UserModel
from app.core.security import get_password_hash, verify_password, create_access_token, decode_access_token
from app.db.session import get_db
from app.utils.exceptions import BadRequestException

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SuccessResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise BadRequestException("이미 등록된 이메일입니다.")
    hashed_password = get_password_hash(user.password)
    new_user = UserModel(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return SuccessResponse(message="회원가입 완료", data={"id": new_user.id, "name": new_user.name, "email": new_user.email})

@router.post("/login", response_model=SuccessResponse)
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise BadRequestException("이메일 또는 비밀번호가 잘못되었습니다.")
    # 토큰 생성
    access_token = create_access_token(data={"sub": db_user.email})
    
    # 응답 헤더에 토큰 포함
    response.headers["Authorization"] = f"Bearer {access_token}"
    
    return SuccessResponse(data=Token(access_token=access_token, token_type="bearer"))

# Current user dependency
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
