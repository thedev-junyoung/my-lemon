# app/tests/test_user.py

import pytest
from fastapi.testclient import TestClient
from app.models.user import User as UserModel
from app.core.auth import get_auth_headers
import uuid

# 사용자 생성 테스트
def test_create_user(test_client: TestClient):
    email = f"testuser_{uuid.uuid4()}@example.com"
    user_data = {"name": "newuser", "email": email, "password": "123123"}
    response = test_client.post("/auth/signup", json=user_data, headers=get_auth_headers(email))
    assert response.status_code == 201
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["email"] == email

# 사용자 목록 조회 테스트
def test_read_users(test_client: TestClient, create_test_user):
    response = test_client.get("/users/", headers=get_auth_headers(create_test_user.email))
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
    assert len(data["data"]) > 0

# 사용자 상세 조회 테스트
def test_read_user(test_client: TestClient, create_test_user):
    response = test_client.get(f"/users/{create_test_user.id}", headers=get_auth_headers(create_test_user.email))
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["email"] == create_test_user.email

# 사용자 업데이트 테스트
def test_update_user(test_client: TestClient, create_test_user):
    update_name='updateduser'
    update_data = {"name": "updateduser", "hashed_password": '12341234'}
    response = test_client.put(
        f"/users/{create_test_user.id}",
        json=update_data,
        headers=get_auth_headers(create_test_user.email)
    )
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["name"] == update_name
    assert data["data"]["email"] == create_test_user.email

# 사용자 삭제 테스트
def test_delete_user(test_client: TestClient, create_test_user):
    response = test_client.delete(f"/users/{create_test_user.id}", headers=get_auth_headers(create_test_user.email))
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1

    # 삭제된 사용자 조회 시 404 오류 반환 확인
    response = test_client.get(f"/users/{create_test_user.id}", headers=get_auth_headers(create_test_user.email))
    assert response.status_code == 404
