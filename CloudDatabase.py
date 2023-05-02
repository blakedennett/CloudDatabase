import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage

# "project_id": "cloud-database-69f2b"

# Application Default credentials are automatically created.
cred = credentials.Certificate(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\secret\key.json')
firebase_admin.initialize_app(cred)


db = firestore.client()




w1 = {
    'date': 512023
}

w2 = {
    'date': 4282023
}

data = [w1, w2]

for record in data:
    rec = db.collection(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\CloudDatabase').document('dat')
    rec.set(record)
