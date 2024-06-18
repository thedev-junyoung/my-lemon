아래는 `FastAPI` 애플리케이션의 `app`, `router`, `middleware`, `api` 흐름을 아스키 아트로 시각화한 것입니다. 이 그림은 각 구성 요소가 어떻게 연결되어 있는지 이해하는 데 도움이 됩니다.

```diff
+-----------------+
| FastAPI App     |
|   main.py       |
|   [app]         |
+--------+--------+
         |
         v
+--------+--------+
| Middlewares     |
|                 |
| - CORS          |
| - Session       |
| - CSP           |
| - CSRF          |
+--------+--------+
         |
         v
+--------+--------+
| Routers         |
|                 |
| - api_v1_router |
+--------+--------+
         |
         v
+--------+--------+
| API Endpoints   |
|                 |
| - /auth         |
|    - login      |
|    - logout     |
|    - refresh    |
|    - csrf-token |
| - /users        |
|    - read_users |
|    - read_user  |
|    - update_user|
|    - delete_user|
+-----------------+

```
### 상세 설명
1. **FastAPI App (main.py)**:
    - 이 파일은 FastAPI 애플리케이션을 설정하고, 미들웨어와 라우터를 포함하는 기본 구성 요소입니다.
    - `app` 객체는 애플리케이션의 루트 객체로, 모든 설정과 기능을 관리합니다.
2. **Middlewares**:
    - **CORS (Cross-Origin Resource Sharing)**: 외부에서 오는 요청을 허용하거나 차단하기 위한 설정.
    - **Session Middleware**: 세션 관리를 위한 미들웨어로, 사용자 데이터를 세션에 저장하고 관리합니다.
    - **CSP (Content Security Policy)**: 콘텐츠 보안 정책을 설정하여 웹사이트의 콘텐츠를 보호합니다.
    - **CSRF (Cross-Site Request Forgery) Middleware**: CSRF 공격을 방지하기 위해 요청의 유효성을 검사합니다.
3. **Routers**:
    - `api_v1_router`는 버전 1의 API 라우터로, 다양한 엔드포인트를 포함하는 주요 라우터입니다. 이 라우터는 `/auth` 및 `/users`와 같은 경로를 관리합니다.
4. **API Endpoints**:
    - **/auth**:
        - `login`: 사용자 인증을 처리하고 JWT 및 CSRF 토큰을 발급합니다.
        - `logout`: 사용자를 로그아웃하고 쿠키에서 JWT를 삭제합니다.
        - `refresh-token`: 리프레시 토큰을 사용하여 새로운 액세스 토큰을 발급합니다.
        - `csrf-token`: CSRF 토큰을 생성하여 클라이언트에게 반환합니다.
    - **/users**:
        - `read_users`: 모든 사용자 목록을 반환합니다.
        - `read_user`: 특정 사용자 정보를 반환합니다.
        - `update_user`: 사용자 정보를 업데이트합니다.
        - `delete_user`: 사용자를 삭제합니다.