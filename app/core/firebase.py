import firebase_admin
from firebase_admin import credentials, firestore

# Load your Firebase credentials
cred = credentials.Certificate("./app/core/config/service-account-file.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to add data to Firestore
def createUser(collection_name: str, user_data: dict):
    # login_id를 document ID로 사용
    db.collection(collection_name).document(user_data['login_id']).set(user_data)

def validateUser(collection_name: str, login_id: str):
    # login_id로 직접 document 조회
    doc = db.collection(collection_name).document(login_id).get()
    print(doc.to_dict())
    return doc.to_dict() if doc.exists else None
