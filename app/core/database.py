import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlite_web import sqlite_web

from app.core.configuation import load_config
from app.domain.models import base

# 환경별 설정 불러오기
config = load_config()

# 데이터베이스 URL 설정
DATABASE_URL = config["database"]["url"]

# SQLAlchemy 세팅
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print(engine)
# if "test.db" in str(engine.url):
#     base.Base.metadata.create_all(bind=engine)
#     print("✅ 데이터베이스 테이블 생성 완료!")
#     conn = sqlite3.connect("test.db")
#     print("✅ SQLite 데이터베이스에 성공적으로 연결되었습니다.")
#     sqlite_web.app.config["DATABASE"] = "test.db"
#     sqlite_web.app.run(debug=True, port=8080)
#     print("✅ SQLite 웹 UI 실행 중: http://127.0.0.1:8080")
# else:
#     print("❌ 'memory'가 포함되어 있지 않습니다.")

def add_to_firebase_example():
    data = {
        "name": "Example",
        "description": "This is an example entry."
    }
    # add_data("example_collection", data)
    print("Data added to Firebase")