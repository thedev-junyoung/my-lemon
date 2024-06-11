from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Union, Optional

# 사용자 정보의 기본 속성을 정의하는 클래스
class UserBase(BaseModel):
    name: str  # 사용자의 이름
    email: EmailStr  # 사용자의 이메일 (EmailStr을 사용해 이메일 형식 검증)

# 사용자 생성 시 필요한 속성을 정의하는 클래스
class UserCreate(UserBase):
    password: str  # 사용자의 비밀번호

# 사용자 업데이트 시 필요한 속성을 정의하는 클래스
# 업데이트 시 필드들을 옵셔널하게 설정
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, description="사용자 이름")
    password: Optional[str] = Field(None, description="사용자 비밀번호")


# 데이터베이스에 저장된 사용자 정보를 정의하는 기본 클래스
class UserInDBBase(UserBase):
    id: int  # 사용자의 고유 ID
    is_active: bool = True  # 사용자의 활성화 상태, 기본값은 True
    created_at: datetime  # 사용자가 생성된 시간
    updated_at: datetime  # 사용자가 마지막으로 업데이트된 시간

    # 이 설정을 통해 Pydantic이 ORM 모델과의 호환성을 유지하도록 함
    class Config:
        from_attributes = True
        # `from_orm` 대신 `from_attributes` 사용
        model_config = {'from_attributes': True}
            

# 클라이언트에 반환할 사용자 정보를 정의하는 클래스
class User(UserInDBBase):
    pass  # UserInDBBase의 속성들을 그대로 사용

# 사용자가 로그인할 때 필요한 속성을 정의하는 클래스
class UserLogin(BaseModel):
    email: EmailStr  # 사용자의 이메일 (EmailStr을 사용해 이메일 형식 검증)
    password: str  # 사용자의 비밀번호


"""
Pydantic 모델 클래스에 대한 주석:
- Pydantic: 데이터 검증과 직렬화를 담당하는 파이썬 라이브러리로, FastAPI에서 자주 사용됩니다.
- BaseModel: 모든 Pydantic 모델은 BaseModel을 상속받아야 하며, 데이터 검증 및 직렬화를 자동으로 처리합니다.
- UserBase: 사용자와 관련된 기본 속성(이름, 이메일)을 정의합니다.
- UserCreate: 사용자를 생성할 때 필요한 추가 속성(비밀번호)을 정의합니다.
- UserUpdate: 사용자를 업데이트할 때 필요한 속성(비밀번호)을 정의합니다.
- UserInDBBase: 데이터베이스에 저장된 사용자 정보를 정의합니다. ORM과 호환성을 유지하기 위해 orm_mode를 설정합니다.
- User: 클라이언트에 반환할 사용자 정보를 정의합니다.
- UserLogin: 사용자 로그인 시 필요한 속성(이메일, 비밀번호)을 정의합니다.
- Token: JWT 액세스 토큰 정보를 정의합니다.
- TokenData: JWT 토큰의 페이로드 데이터를 정의합니다.
"""
