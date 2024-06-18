# app/service/auth_service.py

from app.repository.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User as UserModel
from app.core.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_user_refresh_token,
    generate_csrf_token
)
from app.utils.logger import logger

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: UserCreate) -> UserModel:
        logger.info("Creating user with email: %s", user.email)
        existing_user = self.user_repository.get_user_by_email(user.email)
        if existing_user:
            raise ValueError("이미 등록된 이메일입니다.")
        hashed_password = get_password_hash(user.password)
        return self.user_repository.create_user(user, hashed_password)

    def authenticate_user(self, user: UserLogin) -> UserModel:
        logger.info("Authenticating user with email: %s", user.email)
        db_user = self.user_repository.get_user_by_email(user.email)
        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise ValueError("이메일 또는 비밀번호가 잘못되었습니다.")
        return db_user

    def create_tokens(self, user: UserModel) -> dict:
        access_token = create_access_token(data={"sub": user.email})
        create_refresh_token(user.id, self.user_repository.db)
        csrf_token = generate_csrf_token()
        return {"access_token": access_token, "csrf_token": csrf_token}

    def delete_user_refresh_token(self, user_id: int) -> None:
        self.user_repository.delete_refresh_token(user_id)

    def verify_refresh_token(self, user_id: int) -> UserModel:
        return verify_user_refresh_token(user_id, self.user_repository.db)
