from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.firebase import createUser, validateUser
from app.core.security import verify_password

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
        createUser("users", user.dict())
        return {"message": "회원가입 성공"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login", tags=['router'])
async def login(user: UserLogin):
    try:
        print(user.login_id)
        user_data = validateUser("users", user.login_id)
        print(user_data)
        if not user_data:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        
        # user_data에서 안전한 필드만 선택해서 반환
        safe_user_data = {
            "login_id": user_data.get("login_id"),
        }
        
        return {"message": "로그인 성공", "user_data": safe_user_data}
    except Exception as e:
        print(f"Login error: {str(e)}")  # 에러 로깅 추가
        raise HTTPException(status_code=500, detail=str(e))

