import firebase_admin
from firebase_admin import credentials,firestore
from random import randint
from tqdm import tqdm
cred = credentials.Certificate("/Users/HikoDz/Desktop/Tic-Tac-Toe-codezilla/info_token_db.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://tic-tac-toe-codezilla-default-rtdb.firebaseio.com/'})
db = firestore.client()
# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
# doc_ref = db.collection("users").document("aturing")
# doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

name = input("enter name: ")
me = [str(ord(name[i])) for i in tqdm(range(len(name)))]
mee = "".join(me)


doc_ref = db.collection("users").document(str(mee))
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
