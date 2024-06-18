# exceptions.py

from fastapi import Request

class BaseAppException(Exception):
    status_code: int
    error_message: str
    detail: dict

    def __init__(self, request: Request, status_code: int, error_message: str):
        self.status_code = status_code
        self.error_message = error_message
        self.detail = {
            "errorDetails": {
                "path": request.url.path,
                "method": request.method
            }
        }
class JWTTokenMissingException(BaseAppException):
    def __init__(self):
        error_message = "JWT가 존재하지 않습니다."
        super().__init__(status_code=401, error_message=error_message)

class JWTTokenExpiredException(BaseAppException):
    def __init__(self):
        error_message = "JWT가 만료되었습니다."
        super().__init__(status_code=401, error_message=error_message)

class JWTTokenInvalidException(BaseAppException):
    def __init__(self):
        error_message = "유효하지 않은 JWT입니다."
        super().__init__(status_code=401, error_message=error_message)

class UserNotFoundException(BaseAppException):
    def __init__(self, user_id: int):
        error_message = f"사용자 ID {user_id}를 찾을 수 없습니다."
        super().__init__(status_code=404, error_message=error_message)

class InvalidUserIdException(BaseAppException):
    def __init__(self, user_id: int):
        error_message = f"유효하지 않은 사용자 ID: {user_id}"
        super().__init__(status_code=400, error_message=error_message)

class DatabaseAccessException(BaseAppException):
    def __init__(self, error: str):
        error_message = f"데이터베이스 접근 오류: {error}"
        super().__init__(status_code=500, error_message=error_message)