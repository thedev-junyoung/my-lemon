from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Union

# 공통 속성을 정의하는 기본 클래스
class UserBase(BaseModel):
    name: str  # 사용자명: 문자열
    email: EmailStr  # 이메일: 이메일 문자열로 변경

# 사용자 생성을 위한 클래스, 비밀번호를 포함
class UserCreate(UserBase):
    password: str  # 비밀번호: 문자열

# 사용자 업데이트를 위한 클래스, 비밀번호를 포함
class UserUpdate(UserBase):
    password: str  # 비밀번호: 문자열

# 데이터베이스에 저장된 사용자 정보를 위한 기본 클래스
class UserInDBBase(UserBase):
    id: int  # 사용자 ID: 정수
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True  # ORM과 호환되도록 설정

# 클라이언트에 반환할 사용자 정보를 위한 클래스
class User(UserInDBBase):
    pass  # UserInDBBase를 그대로 상속받아 사용

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Union[str, None] = None  # 이메일로 변경
