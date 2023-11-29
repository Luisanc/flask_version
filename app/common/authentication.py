from firebase_admin import auth
import jwt
from flask import jsonify
from app.config import SECRET_KEY

def authenticate_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        auth.get_user(user.uid)  # Forces Firebase SDK to verify password
        
        # Generate a JWT token
        token = jwt.encode({'userid':user.uid,'email': email, 'admin': True}, SECRET_KEY, algorithm='HS256')
    
        #successful authentication set auth in firebase
        custom_claims = {'admin': True, 'token':token}
        auth.set_custom_user_claims(user.uid, custom_claims)    

        return jsonify({'token': token}), 200 # Return the token as JSON
    except Exception as e:
        print(str(e))
        # Handle authentication errors (e.g., wrong password)
        return jsonify({'error': 'Authentication failed'}), 400
    
""" def verify_role(user_id):
    user = auth.get_user(user_id)
    return user.custom_claims.get('admin', False) """

def validate_token(token:str) -> bool:
    
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token['userid']
        user = auth.get_user(user_id)
        
    except Exception as e:
        print(str(e))
        raise ValueError('Invalid JWT or user not logged in')
    
    return True
    