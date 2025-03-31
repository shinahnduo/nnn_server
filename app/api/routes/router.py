from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.firebase import createUser, validateUser
from app.core.security import verify_password, create_access_token, hash_password
from datetime import timedelta
from fastapi import Depends
from app.core.deps import get_current_user

router = APIRouter(prefix='/auth')

class UserSignup(BaseModel):
    author_id: str
    created_at: str
    email: str
    login_id: str  # Corrected typo here
    password: str
    phone: str
    updated_at: str
    user_id: int
    user_name: str
    description: str

class UserLogin(BaseModel):
    login_id: str
    password: str

@router.post("/singup", tags=['router'])
async def signup(user: UserSignup):
    try:
        user_data = validateUser("users", user.login_id)
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
        user_data = validateUser("users", user.login_id)
        if not user_data:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        if not verify_password(user.password, user_data.get("password", "")):
            raise HTTPException(status_code=401, detail="Invalid username or password")

        # JWT 토큰 생성
        access_token_expires = timedelta(minutes=30)
        token = create_access_token(
            data={"sub": user_data["login_id"]},
            expires_delta=access_token_expires
        )
        
        # 안전한 사용자 데이터 준비
        safe_user_data = {
            "login_id": user_data.get("login_id"),
            "user_name": user_data.get("user_name"),
            "email": user_data.get("email")
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

