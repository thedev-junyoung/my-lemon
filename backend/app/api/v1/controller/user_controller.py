# user_controller.py

from fastapi import APIRouter, Depends, HTTPException, Request
from app.schemas.user import UserUpdate, UserResponse
from app.schemas.response import SuccessResponse
from app.models.user import User as UserModel
from app.service.user_service import UserService
from app.core.dependencies import get_user_service, get_current_user
from app.utils.logger import logger
from app.core.exceptions import UserNotFoundException, InvalidUserIdException, DatabaseAccessException

router = APIRouter()

class UserController:
    def __init__(self):
        logger.info('UserController 클래스 생성')

    @router.get("/users")
    async def read_users(self, user_service: UserService = Depends(get_user_service)):
        try:
            users = user_service.get_users()
            user_data = [UserResponse(**user.model_dump()) for user in users]
            return SuccessResponse(data=user_data, message="사용자 목록을 성공적으로 불러왔습니다.")
        except DatabaseAccessException as e:
            logger.error(f"데이터베이스 접근 오류: {str(e)}")
            raise HTTPException(status_code=500, detail="서버 내부 오류가 발생했습니다.")

    @router.get("/users/{user_id}")
    async def read_user(self, user_id: int, user_service: UserService = Depends(get_user_service)):
        if user_id < 1:
            logger.error(f"잘못된 사용자 ID: {user_id}")
            raise HTTPException(status_code=400, detail=f"유효하지 않은 사용자 ID: {user_id}")

        user = user_service.get_user(user_id)
        if user:
            user_data = UserResponse(**user.model_dump())
            return SuccessResponse(data=user_data, message="사용자를 성공적으로 불러왔습니다.")
        else:
            logger.error(f"사용자 ID {user_id}를 찾을 수 없습니다.")
            raise HTTPException(status_code=404, detail=f"사용자 ID {user_id}를 찾을 수 없습니다.")

    @router.put("/users/{user_id}")
    async def update_user(self, user_id: int, user: UserUpdate, request: Request, user_service: UserService = Depends(get_user_service), current_user: UserModel = Depends(get_current_user)):
        if user_id != current_user.id:
            logger.error(f"현재 사용자와 수정 대상 사용자가 일치하지 않습니다.")
            raise HTTPException(status_code=403, detail="현재 사용자와 수정 대상 사용자가 일치하지 않습니다.")

        updated_user = user_service.update_user(user_id=user_id, user_update=user)
        if updated_user:
            return SuccessResponse(data=updated_user.model_dump(), message="사용자 정보가 성공적으로 업데이트되었습니다.")
        else:
            logger.error(f"사용자 ID {user_id}를 찾을 수 없습니다.")
            raise HTTPException(status_code=404, detail=f"사용자 ID {user_id}를 찾을 수 없습니다.")

    @router.delete("/users/{user_id}")
    async def delete_user(self, user_id: int, user_service: UserService = Depends(get_user_service)):
        if user_id < 1:
            logger.error(f"잘못된 사용자 ID: {user_id}")
            raise HTTPException(status_code=400, detail=f"유효하지 않은 사용자 ID: {user_id}")

        success = user_service.delete_user(user_id)
        if success:
            return SuccessResponse(data=None, message="사용자가 성공적으로 삭제되었습니다.")
        else:
            logger.error(f"사용자 ID {user_id}를 찾을 수 없습니다.")
            raise HTTPException(status_code=404, detail=f"사용자 ID {user_id}를 찾을 수 없습니다.")
