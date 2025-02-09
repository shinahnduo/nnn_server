from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.configuation import load_config

# 환경별 설정 불러오기
config = load_config()

# 데이터베이스 URL 설정
DATABASE_URL = config["database"]["url"]

# SQLAlchemy 세팅
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 테스트용 테이블 정의
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 가져오기
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 데이터 삽입 테스트
def test_insert_user():
    db = SessionLocal()
    new_user = User(name="John Doe", email="johndoe@example.com")
    db.add(new_user)
    db.commit()
    print("✅ User Inserted:", new_user.id, new_user.name, new_user.email)
    db.close()

# 데이터 조회 테스트
def test_select_users():
    db = SessionLocal()
    users = db.query(User).all()
    print("📌 All Users:")
    for user in users:
        print(f"  - ID: {user.id}, Name: {user.name}, Email: {user.email}")
    db.close()

# 데이터 수정 테스트
def test_update_user():
    db = SessionLocal()
    user = db.query(User).filter(User.name == "John Doe").first()
    if user:
        user.email = "john.updated@example.com"
        db.commit()
        print("🔄 User Updated:", user.id, user.name, user.email)
    else:
        print("❌ No User Found to Update")
    db.close()

# 데이터 삭제 테스트
def test_delete_user():
    db = SessionLocal()
    user = db.query(User).filter(User.name == "John Doe").first()
    if user:
        db.delete(user)
        db.commit()
        print("🗑️ User Deleted:", user.id, user.name)
    else:
        print("❌ No User Found to Delete")
    db.close()

# 데이터베이스 테이블 생성 (초기 실행 시 필요)
test_insert_user()    # 데이터 삽입
test_select_users()   # 데이터 조회
test_update_user()    # 데이터 수정
test_select_users()   # 수정된 데이터 확인
test_delete_user()    # 데이터 삭제
test_select_users()   # 삭제 후 데이터 확인