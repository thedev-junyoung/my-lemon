from sqlalchemy.orm import Session
from app.schemas.user import UserUpdate
from app.core.auth import get_password_hash
from app.models.user import User as UserModel
from app.models.refresh_token import RefreshToken
from app.schemas.user import UserCreate
from app.utils.logger import logger

from datetime import datetime, timedelta, timezone


# ORM 개념 설명:
# ORM(Object Relational Mapping)은 객체 지향 프로그래밍 언어를 사용하여 데이터베이스를 조작하는 기술입니다.
# SQLAlchemy는 Python의 ORM 라이브러리로, 데이터베이스 테이블과 Python 클래스를 매핑하여 데이터베이스 작업을 쉽게 할 수 있게 해줍니다.


class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        logger.info('UserRepository 인스턴스 생성됨')

    def get_users(self):
        logger.info('get_users 함수 호출됨')
        return self.db.query(UserModel).all()

    def get_user(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def update_user(self, user_id: int, user_update: UserUpdate):
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            for key, value in user_update.model_dump(exclude_unset=True).items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False
    
    def get_user_by_email(self, email: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def create_user(self, user: UserCreate, hashed_password: str) -> UserModel:
        new_user = UserModel(name=user.name, email=user.email, hashed_password=hashed_password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def delete_refresh_token(self, user_id: int) -> None:
        refresh_token = self.db.query(RefreshToken).filter(
            RefreshToken.user_id == user_id,
            RefreshToken.expires_at >= datetime.now(timezone.utc)
        ).first()
        if refresh_token:
            self.db.delete(refresh_token)
            self.db.commit()
    def delete_refresh_token(self, user_id: int) -> None:
        current_time = datetime.now(timezone.utc)
        refresh_token = self.db.query(RefreshToken).filter(
            RefreshToken.user_id == user_id,
            RefreshToken.expires_at >= current_time
        ).first()
        if refresh_token:
            self.db.delete(refresh_token)
            self.db.commit()
    def get_refresh_token(self, user_id: int) -> RefreshToken:
        return self.db.query(RefreshToken).filter(
            RefreshToken.user_id == user_id,
            RefreshToken.expires_at >= datetime.now(timezone.utc)
        ).first()
    
    
"""
# 모든 사용자를 데이터베이스에서 조회하는 함수
def get_users(db: Session):
    # db.query(User): User 테이블에서 쿼리 생성
    # .all(): 모든 레코드 반환
    return db.query(User).all()

# 특정 사용자를 ID로 조회하는 함수
def get_user(db: Session, user_id: int):
    # db.query(User): User 테이블에서 쿼리 생성
    # .filter(User.id == user_id): 특정 조건(사용자 ID)으로 필터링
    # .first(): 조건에 맞는 첫 번째 레코드 반환
    return db.query(User).filter(User.id == user_id).first()

# 특정 사용자를 이메일로 조회하는 함수
def get_user_by_email(db: Session, email: str):
    # db.query(User): User 테이블에서 쿼리 생성
    # .filter(User.email == email): 특정 조건(이메일)으로 필터링
    # .first(): 조건에 맞는 첫 번째 레코드 반환
    return db.query(User).filter(User.email == email).first()

# 새로운 사용자를 생성하는 함수
def create_user(db: Session, user: UserCreate):
    # 비밀번호 해시화 (암호화)
    hashed_password = get_password_hash(user.password)
    # User 인스턴스 생성 (새 사용자)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    # 데이터베이스에 새 사용자 추가
    db.add(db_user)
    # 변경 사항 커밋 (저장)
    db.commit()
    # 새 사용자 정보를 새로 고침하여 최신 상태 반영
    db.refresh(db_user)
    # 새 사용자 반환
    return db_user

# 기존 사용자를 업데이트하는 함수
def update_user(db: Session, user_id: int, user_update: UserUpdate):
    # ID로 기존 사용자 조회
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    # 사용자 정보 업데이트
    update_data = user_update.model_dump(exclude_unset=True)  # 설정되지 않은 필드 제외
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    for key, value in update_data.items():
        setattr(db_user, key, value)
    # 변경 사항 커밋 (저장)
    db.commit()
    # 업데이트된 사용자 반환
    db.refresh(db_user)
    return db_user

# 사용자를 삭제하는 함수
def delete_user(db: Session, user_id: int):
    # ID로 사용자 조회
    db_user = db.query(User).filter(User.id == user_id).first()
    # 데이터베이스에서 사용자 삭제
    db.delete(db_user)
    # 변경 사항 커밋 (저장)
    db.commit()
    # 삭제된 사용자 반환
    return db_user


"""