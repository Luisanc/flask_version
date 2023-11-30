from firebase_admin import db
from flask import jsonify

"""
Method to get all elements in firebase db

return an object(json) of element in db
"""
def get_all():
    products_ref = db.reference('products')
    all_products = products_ref.get()

    if all_products:
        return jsonify(all_products), 200
    else:
        return jsonify({'message': 'No products found'}), 404