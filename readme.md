# React + FastAPI Boilerplate

## 폴더 구조

```bash
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── v1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dependencies
│   │   │   │   ├── endpoints
│   │   │   │   │   └── user.py
│   │   │   │   ├── routers.py
│   │   │   │   └── utils
│   │   │   │       └── pagination.py
│   │   │   └── v2
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── crud
│   │   │   └── user.py
│   │   ├── db
│   │   │   ├── base.py
│   │   │   ├── base_class.py
│   │   │   └── session.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── post.py
│   │   │   └── user.py
│   │   └── schemas
│   │       ├── post.py
│   │       └── user.py
│   ├── docker-compose.yml
│   ├── mysql-init
│   │   └── init.sql
│   └── requirements.txt
└── frontend
    ├── README.md
    ├── package-lock.json
    ├── package.json
    ├── public
    │   ├── favicon.ico
    │   ├── index.html
    │   ├── logo192.png
    │   ├── logo512.png
    │   ├── manifest.json
    │   └── robots.txt
    ├── src
    │   ├── api
    │   │   └── userApi.ts
        ├── components
        │   ├── Button
        │   │   ├── Button.css
        │   │   └── Button.tsx
        │   ├── ChatContent
        │   │   ├── ChatContent.css
        │   │   └── ChatContent.tsx
        │   ├── ChatInput
        │   │   ├── ChatInput.css
        │   │   └── ChatInput.tsx
        │   ├── Login
        │   │   ├── Login.css
        │   │   └── Login.tsx
        │   ├── Message
        │   │   ├── Message.css
        │   │   └── Message.tsx
        │   └── Sidebar
        │       ├── Sidebar.css
        │       └── Sidebar.tsx
        ├── hooks
        │   └── useChat.ts
        ├── models            # 모델 정의 파일
        ├── pages             # 페이지 컴포넌트
        │   ├── Home
        │   │   ├── Home.css
        │   │   └── Home.tsx
        │   └── Login
        │       ├── Login.css
        │       └── Login.tsx
        ├── schemas           # 스키마 정의 파일
        ├── types             # 타입 정의 파일
        └── utils             # 유틸리티 함수
    │   ├── App.tsx
    │   ├── App.css
    │   ├── index.tsx
    │   ├── index.css
    │   └── react-app-env.d.ts
    ├── tailwind.config.js
    └── tsconfig.json
```

### 백엔드 구조

- `api/v1/endpoints/user.py`: 사용자 관련 CRUD 엔드포인트 정의
- `core/config.py`: 애플리케이션 설정 관리
- `core/security.py`: 보안 관련 설정 및 기능
- `crud/user.py`: 사용자 데이터베이스 CRUD 로직
- `db/session.py`: 데이터베이스 세션 설정
- `db/base.py`: 모든 모델을 등록하여 SQLAlchemy가 이를 인식하고 테이블을 생성할 수 있게 함
- `db/base_class.py`: 데이터베이스 모델의 베이스 클래스를 정의
- `main.py`: FastAPI 애플리케이션 진입점
- `models/user.py`: 사용자 데이터베이스 모델 정의
- `schemas/user.py`: 사용자 Pydantic 스키마 정의

### 프론트엔드 구조

#### 컴포넌트
- `src/components`: 모든 React 컴포넌트를 포함하는 디렉토리입니다.
    - `Button`: 버튼 컴포넌트 및 스타일 (Button.css, Button.tsx)
    - `ChatContent`: 채팅 내용을 표시하는 컴포넌트 및 스타일 (ChatContent.css, ChatContent.tsx)
    - `ChatInput`: 채팅 메시지를 입력하는 컴포넌트 및 스타일 (ChatInput.css, ChatInput.tsx)
    - `Header`: 애플리케이션 헤더 컴포넌트 및 스타일 (Header.css, Header.tsx)
    - `Login`: 로그인 폼 컴포넌트 및 스타일 (Login.css, Login.tsx)
    - `Message`: 개별 채팅 메시지를 표시하는 컴포넌트 및 스타일 (Message.css, Message.tsx)
    - `Sidebar`: 사이드바 컴포넌트 및 스타일 (Sidebar.css, Sidebar.tsx)
- `src/App.tsx`: 메인 React 컴포넌트입니다.
- `src/index.tsx`: React 애플리케이션의 진입점입니다.

#### API
- `src/api/userApi.ts`: 사용자 관련 API 통신 함수를 정의합니다.

#### 모델 및 스키마
- `src/models/user.ts`: 프론트엔드에서 사용하는 사용자 모델을 정의합니다.
- `src/schemas/user.ts`: 사용자 Pydantic 스키마를 정의합니다 (백엔드와 일관성을 위해).

#### 타입
- `src/types/index.ts`: 모든 타입 정의를 포함하는 파일입니다.

#### 유틸리티
- `src/utils/helpers.ts`: 유틸리티 함수를 포함하는 파일입니다.

#### 스타일
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
