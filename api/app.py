import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from api.__init__ import get_key
cred = credentials.Certificate(get_key())
firebase_admin.initialize_app(cred)

db = firestore.client()


def db_con():
    return db



