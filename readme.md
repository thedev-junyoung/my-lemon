# Legal Monster project

## 프로젝트 구조

### 디렉토리 구조

```bash
├── backend
│   ├── alembic
│   │   ├── README
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 0c4874febcf5_initial_migration.py
│   │       ├── b5c2561af5f4_add_profile_img_to_user.py
│   │       ├── cd66a80cf5f8_add_refreshtoken_table.py
│   │       ├── de28faa5494e_remove_unique_constraint_from_name.py
│   │       └── e5e6867e9a1e_add_role_to_user.py
│   ├── alembic.ini
│   ├── app
│   │   ├── __init__.py
│   │   ├── api
│   │   │   └── v1
│   │   │       ├── controller
│   │   │       │   ├── auth_controller.py
│   │   │       │   ├── readme.md
│   │   │       │   └── user_controller.py
│   │   │       └── routers
│   │   │           └── __init__.py
│   │   ├── core
│   │   │   ├── auth.py
│   │   │   ├── config.py
│   │   │   ├── dependencies.py
│   │   │   ├── exceptions.py
│   │   │   └── handlers
│   │   │       └── exception_handlers.py
│   │   ├── db
│   │   │   ├── base.py
│   │   │   ├── base_class.py
│   │   │   └── session.py
│   │   ├── main.py
│   │   ├── middleware
│   │   │   ├── csp.py
│   │   │   └── csrf.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── refresh_token.py
│   │   │   └── user.py
│   │   ├── repository
│   │   │   └── user_repository.py
│   │   ├── schemas
│   │   │   ├── auth.py
│   │   │   ├── response.py
│   │   │   └── user.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── conftest.py
│   │   │   ├── test_auth.py
│   │   │   └── test_user.py
│   │   └── utils
│   │       ├── logger.py
│   │       └── pagination.py
│   ├── docker-compose.yml
│   ├── log
│   │   └── application.log
│   ├── mysql-init
│   │   └── init.sql
│   ├── requirements.txt
│   └── test.db
├── frontend
│   ├── README.md
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── kakao
│   │   │   ├── kakao_login_large_narrow.png
│   │   │   ├── kakao_login_large_wide.png
│   │   │   ├── kakao_login_medium_narrow.png
│   │   │   └── kakao_login_medium_wide.png
│   │   ├── logo
│   │   │   ├── logo100x50.png
│   │   │   ├── logo150x75.png
│   │   │   └── logo200x100.png
│   │   ├── manifest.json
│   │   └── robots.txt
│   ├── src
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── api
│   │   │   ├── axiosInstance.ts
│   │   │   ├── menuActions.tsx
│   │   │   └── mock.ts
│   │   ├── components
│   │   │   ├── Button
│   │   │   │   ├── Button.tsx
│   │   │   │   └── SendBtn.tsx
│   │   │   ├── ChatContent
│   │   │   │   └── ChatContent.tsx
│   │   │   ├── ChatInput
│   │   │   │   └── ChatInput.tsx
│   │   │   ├── Header
│   │   │   │   └── Header.tsx
│   │   │   ├── InputField
│   │   │   │   └── InputField.tsx
│   │   │   ├── Logo
│   │   │   │   └── Logo.tsx
│   │   │   ├── Message
│   │   │   │   └── Message.tsx
│   │   │   └── Sidebar
│   │   │       ├── AdminSidebar.tsx
│   │   │       ├── BottomMenu.tsx
│   │   │       ├── MainSidebar.tsx
│   │   │       ├── MenuItem.tsx
│   │   │       ├── NewSidebar.tsx
│   │   │       ├── Sidebar.tsx
│   │   │       └── SidebarData.ts
│   │   ├── hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useChat.ts
│   │   │   └── useMenuHandler.ts
│   │   ├── index.css
│   │   ├── index.tsx
│   │   ├── models
│   │   ├── pages
│   │   │   ├── Home
│   │   │   │   └── Home.tsx
│   │   │   ├── Login
│   │   │   │   └── Login.tsx
│   │   │   └── SignUp
│   │   │       └── SignUp.tsx
│   │   ├── react-app-env.d.ts
│   │   ├── schemas
│   │   ├── types
│   │   │   └── index.tsx
│   │   └── utils
│   ├── tailwind.config.js
│   └── tsconfig.json
```
## 백엔드 구조

### 주요 디렉토리 및 파일
- **`api/v1/endpoints/`**
    - **`auth.py`**: 사용자 인증 관련 엔드포인트를 정의합니다.
    - **`user.py`**: 사용자 정보 관리와 관련된 엔드포인트를 정의합니다.
- **`core/`**
    - **`auth.py`**: 인증 관련 로직 (JWT 생성, 검증 등)을 포함합니다.
    - **`config.py`**: 애플리케이션 설정을 관리합니다.
    - **`dependencies.py`**: FastAPI 의존성 주입을 위한 함수들을 정의합니다.
- **`repository/`**
    - **`user.py`**: 사용자에 대한 CRUD (생성, 읽기, 업데이트, 삭제) 작업을 정의합니다.
- **`db/`**
    - **`base.py`**: 모든 데이터베이스 모델을 등록하여 SQLAlchemy가 이를 인식할 수 있도록 합니다.
    - **`base_class.py`**: 데이터베이스 모델의 기본 클래스를 정의합니다.
    - **`session.py`**: 데이터베이스 세션을 설정합니다.
- **`main.py`**: FastAPI 애플리케이션의 진입점입니다.
- **`middleware/`**
    - **`csrf.py`**: CSRF 토큰을 검증하는 미들웨어를 정의합니다.
    - **`csp.py`**: Content Security Policy(CSP) 설정을 관리하는 미들웨어입니다.
- **`models/`**
    - **`user.py`**: 사용자 데이터베이스 모델을 정의합니다.
    - **`refresh_token.py`**: 리프레시 토큰 모델을 정의합니다.
- **`schemas/`**
    - **`auth.py`**: 사용자 인증 관련 Pydantic 스키마를 정의합니다.
    - **`response.py`**: 표준 응답 구조를 정의합니다.
    - **`user.py`**: 사용자 관련 Pydantic 스키마를 정의합니다.
- **`tests/`**
    - **`auth.py`**: 인증 관련 테스트를 포함합니다.
    - **`conftest.py`**: 테스트 환경 설정을 포함합니다.
    - **`test_auth.py`**: 사용자 인증 API에 대한 테스트를 포함합니다.
    - **`test_user.py`**: 사용자 관리 API에 대한 테스트를 포함합니다.
- **`utils/`**
    - **`logger.py`**: 로깅 유틸리티를 포함합니다.
    - **`pagination.py`**: 페이징 유틸리티를 포함합니다.
- **`alembic/`**
    - **`versions/`**: 데이터베이스 스키마의 버전 관리 파일이 위치합니다.
        - **`0c4874febcf5_initial_migration.py`**: 초기 데이터베이스 마이그레이션 파일입니다.
        - **`b5c2561af5f4_add_profile_img_to_user.py`**: 사용자 테이블에 프로필 이미지를 추가하는 마이그레이션 파일입니다.
        - **`cd66a80cf5f8_add_refreshtoken_table.py`**: 리프레시 토큰 테이블을 추가하는 마이그레이션 파일입니다.
        - **`de28faa5494e_remove_unique_constraint_from_name.py`**: 이름 필드에서 유니크 제약 조건을 제거하는 마이그레이션 파일입니다.
        - **`e5e6867e9a1e_add_role_to_user.py`**: 사용자 테이블에 역할(role)을 추가하는 마이그레이션 파일입니다.

### Alembic 디렉토리 구조 및 설명
Alembic은 SQLAlchemy 기반 애플리케이션에서 데이터베이스 스키마의 버전 관리를 지원하는 도구입니다. 이를 통해 데이터베이스 스키마의 변경 사항을 추적하고, 일관되게 관리할 수 있습니다.
- `alembic/env.py`: Alembic 설정 파일. 데이터베이스 연결 및 마이그레이션 환경을 설정합니다.
- `alembic/script.py.mako`: Alembic 마이그레이션 스크립트 템플릿 파일.
- `alembic/versions/`: 버전별 마이그레이션 파일이 저장되는 디렉토리.
    - `0c4874febcf5_initial_migration.py`: 초기 마이그레이션 파일. 데이터베이스 스키마 생성 내용을 포함.
    - `de28faa5494e_remove_unique_constraint_from_name.py`: 특정 변경 사항을 반영한 마이그레이션 파일.
- `alembic.ini`: Alembic 기본 설정 파일. 데이터베이스 URL, 스크립트 위치 등을 설정합니다.


## 프론트엔드 구조

### 컴포넌트
- **`src/components/`**: 모든 React 컴포넌트를 포함하는 디렉토리입니다.
    
    - **`Button`**: 버튼 컴포넌트 및 스타일 정의
    - **`ChatContent`**: 채팅 내용을 표시하는 컴포넌트 정의
    - **`ChatInput`**: 채팅 메시지를 입력하는 컴포넌트 정의
    - **`Header`**: 애플리케이션 헤더 컴포넌트 정의
    - **`Logo`**: 로고 컴포넌트 정의
    - **`Message`**: 개별 채팅 메시지를 표시하는 컴포넌트 정의
    - **`Sidebar`**: 사이드바 컴포넌트 정의
    - **`InputField`**: 입력 필드 컴포넌트 정의
- **`src/api/`**: API 호출 관련 파일
    
    - **`axiosInstance.ts`**: Axios 인스턴스를 설정하여 API 요청을 관리합니다.
    - **`menuActions.tsx`**: 메뉴 관련 API 액션 정의
    - **`mock.ts`**: API 모킹 설정
- **`src/hooks/`**: 커스텀 훅 정의
    
    - **`useAuth.ts`**: 인증 관련 커스텀 훅
    - **`useChat.ts`**: 채팅 관련 커스텀 훅
    - **`useMenuHandler.ts`**: 메뉴 클릭 핸들러 커스텀 훅
- **`src/pages/`**: 주요 페이지 컴포넌트
    
    - **`Home`**: 홈 페이지 컴포넌트
    - **`Login`**: 로그인 페이지 컴포넌트
    - **`SignUp`**: 회원가입 페이지 컴포넌트
- **`src/models/`**: 프론트엔드에서 사용하는 데이터 모델 정의
    
- **`src/schemas/`**: 프론트엔드에서 사용하는 스키마 정의
    
- **`src/types/`**: 타입 정의 파일
    
- **`src/utils/`**: 유틸리티 함수 정의 파일
    
- **`src/index.tsx`**: React 애플리케이션의 진입점입니다.
    
- **`src/App.tsx`**: 메인 React 컴포넌트입니다.
    
- **`public/`**: 정적 파일 (이미지, HTML 파일 등)을 포함하는 디렉토리입니다.
    

### API

- `src/api/axiosInstance.ts`: Axios 인스턴스를 설정하여 API 요청을 관리합니다.
- `src/api/menuActions.tsx`: 메뉴 관련 API 액션 정의
- `src/api/mock.ts`: API 모킹 설정

### Hooks

- `src/hooks/useAuth.ts`: 인증 관련 커스텀 훅
- `src/hooks/useChat.ts`: 채팅 관련 커스텀 훅
- `src/hooks/useMenuHandler.ts`: 메뉴 클릭 핸들러 커스텀 훅

### 모델 및 스키마

- `src/models/user.ts`: 프론트엔드에서 사용하는 사용자 모델을 정의합니다.
- `src/schemas/user.ts`: 사용자 Pydantic 스키마를 정의합니다 (백엔드와 일관성을 위해).

### 타입

- `src/types/index.ts`: 모든 타입 정의를 포함하는 파일입니다.

### 유틸리티

- `src/utils/helpers.ts`: 유틸리티 함수를 포함하는 파일입니다.

### 스타일

- `src/App.css`: 메인 React 컴포넌트의 스타일을 정의합니다.
- `src/index.css`: 전역 스타일을 정의합니다.

### 설정 및 실행

#### 요구 사항

- Docker
- Docker Compose
- Node.js (v14 이상)
- Python (3.9 이상)

#### 백엔드 설정 및 실행

1. **백엔드 의존성 설치**

```bash
cd backend && python3.9 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

2. **Docker 컨테이너 실행**

```bash
docker-compose up --build
```

3. **FastAPI 서버 실행**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### 프론트엔드 설정 및 실행

1. **프론트엔드 의존성 설치**

```bash
cd frontend && npm install
```

2. **React 애플리케이션 실행**

```bash
npm start
```

React 개발 서버가 `http://localhost:3000`에서 실행됩니다.

### 주요 기능

- **사용자 생성**: 사용자를 생성하는 API와 폼 제공
- **사용자 조회**: 전체 사용자 목록을 조회하는 API와 리스트 컴포넌트 제공
- **사용자 업데이트**: 사용자를 업데이트하는 API와 폼 제공
- **사용자 삭제**: 사용자를 삭제하는 API와 버튼 제공

### API 엔드포인트

- `GET /api/v1/users/`: 전체 사용자 목록 조회
- `POST /api/v1/users/`: 새 사용자 생성
- `GET /api/v1/users/{user_id}`: 특정 사용자 조회
- `PUT /api/v1/users/{user_id}`: 특정 사용자 업데이트
- `DELETE /api/v1/users/{user_id}`: 특정 사용자 삭제

### 주의 사항

- 환경 변수 설정은 `.env` 파일을 사용하여 관리합니다.
- 데이터베이스 초기화 스크립트는 `mysql-init/init.sql` 파일을 사용합니다.
- 개발 환경에서는 `DEBUG` 모드를 활성화하세요.
