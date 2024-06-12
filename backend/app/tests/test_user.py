# tests/test_user.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.session import Base, get_db
from app.models.user import User as UserModel
from app.core.auth import create_access_token, generate_csrf_token, get_auth_headers
from datetime import timedelta

# 테스트용 SQLite 인메모리 데이터베이스 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 테이블 초기화
Base.metadata.create_all(bind=engine)

# 테스트 데이터베이스 종속성 덮어쓰기
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# 사용자를 위한 테스트 데이터 생성
@pytest.fixture
def create_test_user():
    db = TestingSessionLocal()
    user = UserModel(name="testuser", email="testuser@example.com", hashed_password="hashed_password")
    db.add(user)
    db.commit()
    db.refresh(user)
    yield user
    db.delete(user)  # 테스트 후 데이터 삭제
    db.commit()
    db.close()

# 사용자 목록 조회 테스트
def test_read_users(create_test_user):
    response = client.get("/users/", headers=get_auth_headers())
    assert response.status_code == 200
    data = response.json()
    print("response.json():",response.json())
    assert data["code"] == 1
    assert len(data["data"]) > 0

# 사용자 상세 조회 테스트
def test_read_user(create_test_user):
    response = client.get(f"/users/{create_test_user.id}", headers=get_auth_headers())
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["name"] == "testuser"

# 사용자 생성 테스트
def test_create_user():
    user_data = {"name": "newuser", "email": "new2@example.com", "password": "123123"}
    response = client.post("/auth/signup", json=user_data, headers=get_auth_headers())
    print('response.status_code',response.status_code)
    assert response.status_code == 201
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["name"] == "newuser"

# 사용자 업데이트 테스트
def test_update_user(create_test_user):
    update_data = {"name": "updateduser", "email": "updated@example.com"}
    response = client.put(
        f"/users/{create_test_user.id}",
        json=update_data,
        headers=get_auth_headers()
    )
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["name"] == "updateduser"

# 사용자 삭제 테스트
def test_delete_user(create_test_user):
    response = client.delete(f"/users/{create_test_user.id}", headers=get_auth_headers())
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1

    # 삭제된 사용자 조회 시 404 오류 반환 확인
    response = client.get(f"/users/{create_test_user.id}", headers=get_auth_headers())
    assert response.status_code == 404
    expected_response = {
        "code": 0,
        "errors": "404",
        "message": "요청한 리소스를 찾을 수 없습니다.",
        "status": "error"
    }
    assert response.json() == expected_response
