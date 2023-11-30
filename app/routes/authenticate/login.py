from app import app
from flask import abort, request
from app.common.authentication import validate_token, authenticate_user

@app.route('/login', methods=['POST'])
def login():
    if not request.json or 'email' not in request.json or 'password' not in request.json:
        abort(400)  # Bad request if required fields are missing

    email = request.json['email']
    password = request.json['password']
    
    return authenticate_user(email=email, password=password)