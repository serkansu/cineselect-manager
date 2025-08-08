# firebase_setup.py
import firebase_admin
from firebase_admin import credentials, firestore

def get_firestore():
    if not firebase_admin._apps:
        cred = credentials.Certificate("firebase-adminsdk.json")  # JSON dosyanın ismi buysa değişme!
        firebase_admin.initialize_app(cred)
    return firestore.client()
