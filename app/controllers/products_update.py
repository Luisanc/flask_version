from firebase_admin import db
from app.models.product import Product
from flask import jsonify
    
"""
Method to update a registry in firebase db
product_id: uuid(string)
product_item -> product model include fields
{
    'sku': string,
    'name': string,
    'price': float,
    'brand': string,
    'stock': integer
}

return json of updated element in db
"""
def update_by_id(product_id:str,product_item:Product):
    
    if not product_item.is_valid():
        raise ValueError('Invalid datatype product')
    
    products_ref = db.reference('products')
    product = products_ref.child(product_id).get()

    if product:
        # Update the product data with the new values from request.json
        new_product_data = product_item.to_dict()
        products_ref.child(product_id).update(new_product_data)
        
        updated_product = products_ref.child(product_id).get()
        return jsonify(updated_product), 200
    else:
        return jsonify({'message': 'Product not found'}), 404