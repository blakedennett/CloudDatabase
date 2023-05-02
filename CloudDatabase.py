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
    'date': 522023,
    'type': 'for time',
    '1':'2000m row'
}

w2 = {
    'date': 512023,
    'type': 'amrap',
    '1':'60 cal row',
    '2':'50 ttb',
    '3':'40 wallballs',
    '4':'30 cleans (135/95)',
    '5':'20 ring muscle ups'
}

data = [w1]

def put_data(data_dict, doc_str):
    for record in data_dict:
        write_ref = db.collection(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\CloudDatabase').document(doc_str)
        write_ref.set(record)


put_data(data, 'workouts')






def read_data(id):
    read_ref = db.collection(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\CloudDatabase')
    docs = read_ref.stream()
    for doc in docs:
        if doc.id == id:
            print(doc.to_dict())

# read_data('dat')