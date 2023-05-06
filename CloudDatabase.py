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
w3 = {
    'date':432023,
    'type':'strength',
    'movement':'dead lift, hang clean, front squat, split jerk',
    'weight':175
}
m1 = {
    'date':4182023,
    'movement':'hang clean',
    'weight': 175
}

data1 = [w1]
data2 = [w2]
data3 = [w3]
data4 = [m1]



# the "create_document" function takes in a list with one or more dictionaries and 
# adds them to the given collection
def create_document(data_dict, doc_name, collection):
    for record in data_dict:
        write_ref = db.collection(collection).document(doc_name).collection('maxes').document('hang clean')
        write_ref.set(record)


# create_document(data1, '522023', 'workouts')
# create_document(data2, '512023', 'workouts')
# create_document(data3, '432023', 'workouts')

# create_document(data4, 'hang clean', 'maxes')
# create_document(data3, '432023', 'workouts')





# read_data takes in an id and then prints the dictionary 
def read_document(collection, id):
    read_ref = db.collection(collection)
    docs = read_ref.stream()
    for doc in docs:
        if doc.id == id:
            print(doc.to_dict())

# read_document('workouts', '512023')






# deleting a document
db.collection('workouts').document('522023').delete()









# .collection('maxes').document('hang clean')