from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Load configurations
app.config.from_pyfile('config.py')

# Import routes
from app import routes
