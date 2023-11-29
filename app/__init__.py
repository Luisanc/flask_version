from flask import Flask
import firebase_admin
from firebase_admin import credentials


app = Flask(__name__)

# Load configurations
app.config.from_pyfile('config.py')

# Initialize Firebase app
cred = credentials.Certificate("zebbra-8dc5b-firebase-adminsdk-57882-50d11f73c1.json")  # Path to your Firebase service account key JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': app.config['FIREBASE_CONFIG']['databaseURL']
})

from app import routes