# tests/test_auth.py

import pytest
from fastapi.testclient import TestClient
from app.core.auth import get_auth_headers

# 사용자 회원가입 테스트
def test_signup(test_client: TestClient):
    user_data = {"name": "newuser", "email": "newuser@example.com", "password": "123456"}
    response = test_client.post("/auth/signup", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["code"] == 1
    assert data["data"]["email"] == "newuser@example.com"

# 사용자 로그인 테스트
def test_login(test_client: TestClient):
    login_data = {"email": "newuser@example.com", "password": "123456"}
    response = test_client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1

# CSRF 토큰 생성 테스트
def test_get_csrf_token(test_client: TestClient):
    response = test_client.get("/auth/csrf-token")
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
    assert "csrf_token" in data["data"]

# 토큰 갱신 테스트
def test_refresh_token(test_client: TestClient):
    # 토큰 갱신을 위한 사전 설정
    refresh_data = {"id": 1}
    headers = get_auth_headers("newuser@example.com")  # user_email을 인자로 제공
    response = test_client.post("/auth/refresh-token", json=refresh_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 1
