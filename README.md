📸 Momento - Backend

"하루하루의 순간을 사진과 기록으로 남기고, AI가 이를 정리해주는 감성 일기 앱"

Momento는 사용자가 일상의 사진과 짧은 글을 남기면, 이를 기반으로 AI가 내용을 보정하고 요약해 주는 퍼스널 다이어리 플랫폼입니다. 이 저장된 기록들은 타임라인 기반으로 관리되며, 여행, 일상, 감정 태그 등으로 분류가 가능합니다.

🔧 기술 스택
영역	기술
언어	Python 3.11
웹 프레임워크	FastAPI
인증	JWT, Firebase Authentication
데이터베이스	Firebase Firestore
AI 기능	OpenAI GPT-4 API
배포	Railway / Vercel (프론트), Capacitor (모바일 앱)
기타	CORS, 환경변수 설정 (.env), async 기반 비동기 처리
📂 주요 폴더 구조
📦 backend/
├── main.py                  # FastAPI 진입점
├── routers/
│   ├── auth.py              # 로그인/회원가입/인증 관련
│   ├── entries.py           # 사용자 일기 CRUD
│   └── ai.py                # AI 요약/보정 기능
├── services/
│   ├── firebase_service.py  # Firebase 연동 모듈
│   └── ai_service.py        # GPT API 처리
├── models/
│   ├── user.py              # 유저 모델
│   └── entry.py             # 일기 모델
├── utils/
│   └── helpers.py           # 유틸 함수
├── requirements.txt
└── .env

🚀 주요 기능
1. 📸 일기 업로드 (사진 + 텍스트)

사용자는 사진, 제목, 본문을 업로드할 수 있으며, Firestore에 저장됩니다.

2. ✨ AI 요약 및 보정

업로드된 텍스트를 AI가 감성적으로 요약/보정합니다.

예: "오늘 비가 왔다" → "차분한 빗소리에 마음도 촉촉해졌던 하루"

GPT API를 비동기 처리로 호출

3. 🔐 사용자 인증

Firebase Authentication (이메일/비밀번호 기반)

JWT 토큰 기반 인증으로 FastAPI에서 보호된 API 접근 제어

4. 🧾 일기 리스트 조회 (타임라인)

날짜 순으로 정렬된 기록을 보여주는 API

월별/카테고리별 필터링 기능 지원 예정

🔐 환경변수 (.env)
FIREBASE_PROJECT_ID=xxxx
FIREBASE_API_KEY=xxxx
OPENAI_API_KEY=sk-xxxx
CORS_ORIGINS=http://localhost:3000,https://momento.app
JWT_SECRET_KEY=supersecretkey
PORT=8000

🔍 API 엔드포인트 예시
메소드	경로	설명
POST	/api/auth/signup	회원가입
POST	/api/auth/login	로그인
POST	/api/entries	일기 업로드
GET	/api/entries	사용자 일기 목록 조회
GET	/api/entries/{id}	특정 일기 상세
POST	/api/ai/summarize	AI 요약 요청
🧪 로컬 실행 방법
# 의존성 설치
pip install -r requirements.txt

# 로컬 서버 실행
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

📦 배포

Railway를 통한 FastAPI 서버 배포

Firebase Firestore 및 인증 설정 필요

프론트엔드는 React 기반으로 Vercel 또는 Capacitor를 통해 PWA/Android 앱으로 빌드됨

✅ TODO

 알림 기능 (Firebase Cloud Messaging)

 태그 기반 필터링

 일기 공유 (링크로 친구에게 보내기)

 감정 분석 및 시각화

🙌 기여자

백엔드: sjoongh, annbat

프론트엔드: sjoongh, annbat
