from firebase_admin import db
from flask import jsonify

"""
Method to get element by uuid recibed in firebase db

return json of element in db
"""
def get_by_id(product_id:str):
    products_ref = db.reference('products')
    product = products_ref.child(product_id).get()
    
    if product:
        return jsonify(product), 200
    else:
        return jsonify({'message': 'Product not found'}), 404