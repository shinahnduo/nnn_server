import firebase_admin
from firebase_admin import credentials, firestore

# Load your Firebase credentials
cred = credentials.Certificate("./app/core/config/service-account-file.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Function to add data to Firestore
def add_data(collection_name, data):
    db.collection(collection_name).add(data) 