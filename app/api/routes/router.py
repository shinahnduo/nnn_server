from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.core.firebase import createUser, validateUser
from app.core.security import verify_password, create_access_token, hash_password
from datetime import timedelta
from fastapi import Depends
from app.core.deps import get_current_user
from google.oauth2 import id_token
from google.auth.transport import requests

router = APIRouter(prefix='/auth')

class UserSignup(BaseModel):
    email: str
    created_at: str
    password: str
    phone: str
    updated_at: str
    user_id: int
    user_name: str
    description: str

class UserLogin(BaseModel):
    email: str
    password: str

class GoogleLoginRequest(BaseModel):
    client_id: str
    email: str
    name: str

@router.post("/singup", tags=['router'])
async def signup(user: UserSignup):
    try:
        user_data = validateUser("users", user.email)
        if user_data:
            raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")
        
        # 비밀번호 해시화
        user_dict = user.dict()
        user_dict["password"] = hash_password(user.password)
        
        createUser("users", user_dict)
        return {"message": "회원가입 성공"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login", tags=['router'])
async def login(user: UserLogin):
    try:
        user_data = validateUser("users", user.email)
        if not user_data:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        if not verify_password(user.password, user_data.get("password", "")):
            raise HTTPException(status_code=401, detail="Invalid username or password")

        # JWT 토큰 생성
        access_token_expires = timedelta(minutes=30)
        token = create_access_token(
            data={"sub": user_data["email"]},
            expires_delta=access_token_expires
        )
        
        # 안전한 사용자 데이터 준비
        safe_user_data = {
            "email": user_data.get("email"),
            "user_name": user_data.get("user_name")
        }
        
        return {
            "message": "로그인 성공",
            "token": token,
            "user_data": safe_user_data
        }
    except Exception as e:
        print(f"Login error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/protected", tags=['router'])
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": current_user}

@router.post("/google-login", tags=['router'])
async def google_login(request: GoogleLoginRequest):
    try:
        # ID 토큰 검증
        # idinfo = id_token.verify_oauth2_token(
        #     request.id_token,
        #     requests.Request(),
        #     request.client_id
        # )

        # 클라이언트 ID 확인
        # if idinfo['aud'] != settings.GOOGLE_CLIENT_ID:
        #     raise HTTPException(
        #         status_code=400,
        #         detail="Invalid client ID"
        #     )

        # 이메일 도메인 검증
        # if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        #     raise HTTPException(
        #         status_code=400,
        #         detail="Wrong issuer"
        #     )

        # 사용자 정보 추출
        email = request.email
        name = request.name

        # Firebase에서 사용자 확인
        user_data = validateUser("users", email)

        if not user_data:
            print('here??or')
            # 새 사용자 생성
            new_user = {
                "email": email,
                "user_name": name,
                "created_at": "",  # 현재 시간 설정 필요
                "updated_at": "",
                "user_id": 0,  # 적절한 user_id 생성 로직 필요
                "description": "",
                "phone": ""
            }
            createUser("users", new_user)
            user_data = new_user

        # JWT 토큰 생성
        access_token_expires = timedelta(minutes=30)
        token = create_access_token(
            data={"sub": email},
            expires_delta=access_token_expires
        )

        # 응답 데이터 준비
        safe_user_data = {
            "email": user_data.get("email"),
            "user_name": user_data.get("user_name")
        }

        return {
            "token": token,
            "user_data": safe_user_data
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid token: {str(e)}"
        )
    except Exception as e:
        print(f"Google login error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

