from pydantic import BaseModel

class TokenRefreshRequest(BaseModel):
    id: int  # 사용자 ID
