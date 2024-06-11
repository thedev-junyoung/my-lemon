# app/api/v1/endpoints/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.user import get_user, update_user, delete_user, get_users
from app.schemas.user import User, UserUpdate
from app.schemas.response import SuccessResponse
from app.core.dependencies import get_current_token, get_http_exception_handler
from typing import List

router = APIRouter()

@router.get("/", response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def read_users(db: Session = Depends(get_db), token: dict = Depends(get_current_token)):
    users = get_users(db=db)
    users_data = [User.model_validate(user.__dict__) for user in users]
    return SuccessResponse(data=users_data, message="사용자 목록을 성공적으로 불러왔습니다.")

@router.get("/{user_id}", response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def read_user(user_id: int, db: Session = Depends(get_db), token: dict = Depends(get_current_token)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    user_data = User.model_validate(db_user.__dict__)
    return SuccessResponse(data=user_data, message="사용자를 성공적으로 불러왔습니다.")

@router.put("/{user_id}", response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db), token: dict = Depends(get_current_token)):
    if user_id < 1:
        raise HTTPException(status_code=400, detail="유효하지 않은 사용자 ID입니다.")
    updated_user = update_user(db=db, user_id=user_id, user_update=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    user_data = User.model_validate(updated_user.__dict__)
    return SuccessResponse(data=user_data, message="사용자 정보가 성공적으로 업데이트되었습니다.")

@router.delete("/{user_id}", response_model=SuccessResponse, dependencies=[Depends(get_http_exception_handler)])
def update_user_endpoint(user_id: int, db: Session = Depends(get_db), token: dict = Depends(get_current_token)):
    if user_id < 1:
        raise HTTPException(status_code=400, detail="유효하지 않은 사용자 ID입니다.")
    deleted_user = delete_user(db=db, user_id=user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="사용자를 삭제할 수 없습니다.")
    return SuccessResponse(data=None, message="사용자가 성공적으로 삭제되었습니다.")
