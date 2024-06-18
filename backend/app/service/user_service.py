# user_service.py

from app.repository.user_repository import UserRepository
from app.schemas.user import UserUpdate, UserResponse
from app.models.user import User
from typing import List, Optional
from app.core.exceptions import UserNotFoundException, InvalidUserIdException, DatabaseAccessException

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self) -> List[UserResponse]:
        try:
            users = self.user_repository.get_users()
            return [UserResponse(**user.__dict__) for user in users]
        except Exception as e:
            raise DatabaseAccessException(str(e))

    def get_user(self, user_id: int) -> Optional[UserResponse]:
        if user_id < 1:
            raise InvalidUserIdException(user_id)
        try:
            user = self.user_repository.get_user(user_id)
            if user is None:
                raise UserNotFoundException(user_id)
            return UserResponse(**user.__dict__)
        except UserNotFoundException:
            raise
        except Exception as e:
            raise DatabaseAccessException(str(e))

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[UserResponse]:
        if user_id < 1:
            raise InvalidUserIdException(user_id)
        try:
            user = self.user_repository.update_user(user_id, user_update)
            if user is None:
                raise UserNotFoundException(user_id)
            return UserResponse(**user.__dict__)
        except UserNotFoundException:
            raise
        except Exception as e:
            raise DatabaseAccessException(str(e))

    def delete_user(self, user_id: int) -> bool:
        if user_id < 1:
            raise InvalidUserIdException(user_id)
        try:
            success = self.user_repository.delete_user(user_id)
            if not success:
                raise UserNotFoundException(user_id)
            return True
        except UserNotFoundException:
            raise
        except Exception as e:
            raise DatabaseAccessException(str(e))
