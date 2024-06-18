# app/api/v1/routers/router_manager.py
from fastapi import APIRouter, Depends
from app.api.v1.controller.user_controller import UserController
from app.api.v1.controller.auth_controller import AuthController
from app.core.dependencies import get_current_user, get_user_service, get_auth_service

class RouterManager:
    def __init__(self):
        self.api_router = APIRouter()
        self.include_auth_router()
        self.include_user_router()

    def include_user_router(self):
        user_controller = UserController()
        user_router = APIRouter(
            prefix="/users",
            tags=["users"],
            dependencies=[Depends(get_current_user)]
        )
        user_router.add_api_route("/", user_controller.read_users, methods=["GET"])
        user_router.add_api_route("/{user_id}", user_controller.read_user, methods=["GET"])
        user_router.add_api_route("/{user_id}", user_controller.update_user, methods=["PUT"])
        user_router.add_api_route("/{user_id}", user_controller.delete_user, methods=["DELETE"])

        self.api_router.include_router(user_router)

    def include_auth_router(self):
        auth_controller = AuthController()
        auth_router = APIRouter(
            prefix="/auth",
            tags=["auth"],
            dependencies=[]
        )
        auth_router.add_api_route("/signup", auth_controller.create_user, methods=["POST"])
        auth_router.add_api_route("/login", auth_controller.login, methods=["POST"])
        auth_router.add_api_route("/logout", auth_controller.logout, methods=["POST"])
        auth_router.add_api_route("/refresh-token", auth_controller.refresh_access_token, methods=["POST"])
        auth_router.add_api_route("/csrf-token", auth_controller.get_csrf_token, methods=["GET"])

        self.api_router.include_router(auth_router)

    def get_router(self) -> APIRouter:
        return self.api_router