import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


# "project_id": "cloud-database-69f2b"



# uses credentials from a file that holds the private key
cred = credentials.Certificate(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\secret\key.json')
# stores configuration and administration
firebase_admin.initialize_app(cred)
db = firestore.client()



# two workouts to be placed in the "workouts" document
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

data = [w2]


# the "create_document" function takes in a list with one or more dictionaries and 
# adds them to the given collection
def create_document(data_dict, doc_name, collection):
    for record in data_dict:
        write_ref = db.collection(collection).document(doc_name)
        write_ref.set(record)


# create_document(data, '512023', 'workouts')





# read_data takes in an id and then prints the dictionary 
def read_data(id):
    read_ref = db.collection(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\CloudDatabase')
    docs = read_ref.stream()
    for doc in docs:
        if doc.id == id:
            print(doc.to_dict())

# read_data('dat')