from firebase_admin import db
from flask import jsonify

"""
Method to remove element by uuid recibed in firebase db

return message of confirmation
"""    
def delete_by_id(product_id:str):
    products_ref = db.reference('products')
    product = products_ref.child(product_id).get()
    
    if product:
        products_ref.child(product_id).delete()
        return jsonify({'message': f'Product {product_id} deleted successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404