import firebase_admin
from firebase_admin import credentials, firestore

# Load your Firebase credentials
cred = credentials.Certificate("./app/core/config/service-account-file.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to add data to Firestore
def createUser(collection_name: str, user_data: dict):
    # email document ID로 사용
    db.collection(collection_name).document(user_data['email']).set(user_data)

def validateUser(collection_name: str, email: str):
    # email 직접 document 조회
    doc = db.collection(collection_name).document(email).get()
    return doc.to_dict() if doc.exists else None
