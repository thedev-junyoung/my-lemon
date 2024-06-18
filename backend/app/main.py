# main.py

import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from starlette.middleware.sessions import SessionMiddleware
from fastapi.exceptions import RequestValidationError
from app.core.config import settings
from app.api.v1.routers import RouterManager
from app.db.session import create_tables, engine
from app.db.base import Base
from app.core.config import settings
from app.core.handlers.exception_handlers import base_app_exception_handler, http_exception_handler
from app.middleware.csp import csp_middleware
from app.middleware.csrf import CSRFMiddleware
from app.core.exceptions import BaseAppException


app = FastAPI()

# === CORS 설정 =================================================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,  # 실제 운영 환경에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 필요한 메소드만 허용
    allow_headers=["Authorization", "Content-Type"],  # 필요한 헤더만 허용
    expose_headers=["X-CSRF-Token"]  # expose_headers 추가
)

# === 미들웨어 ==================================================================================
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")  # 세션 미들웨어 추가

@app.middleware("http")
async def csp_middleware_wrapper(request: Request, call_next):
    """CSP 미들웨어 래퍼 함수"""
    return await csp_middleware(request, call_next)

app.add_middleware(CSRFMiddleware)  # CSRF 미들웨어 추가

# === 데이터베이스 및 Lifespan 설정 ============================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션의 lifespan 이벤트 핸들러 정의"""
    Base.metadata.create_all(bind=engine)
    yield
    # 종료 시 수행할 작업이 있으면 여기에 추가

create_tables()  # 데이터베이스 테이블 생성

# === 라우터 및 예외 처리 =========================================================================
router_manager = RouterManager()
app.include_router(router_manager.get_router())

# 전역 예외 핸들러 등록
app.add_exception_handler(BaseAppException, base_app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)



# === 기본 라우트 ============================================================================
@app.get("/")
def read_root():
    """기본 라우트"""
    return {"message": "Hello, World!"}

# === 주석 처리된 패키징 관련 코드 =============================================================
"""
# React 빌드 디렉토리 경로 설정 및 정적 파일 제공 예시
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

build_path = Path(__file__).parent.parent.parent / "frontend" / "build"

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_react_app(full_path: str):
    return (build_path / "index.html").read_text()

app.mount("/static", StaticFiles(directory=build_path / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_react_app():
    return (build_path / "index.html").read_text()
"""
