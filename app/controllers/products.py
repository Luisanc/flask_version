from firebase_admin import db
from app.models.product import Product
from flask import jsonify

"""
Method to create a registry in firebase db
product model include fields
{
    'sku': string,
    'name': string,
    'price': float,
    'brand': string,
    'stock': integer
}

return uuid(String) of element created in db
"""
def create_product(product_item:Product):
    
    if not product_item.is_valid():
        raise ValueError('Invalid datatype product')
    
    products_ref = db.reference('products')
    # Create a new product entry
    new_product_ref = products_ref.push(product_item.to_dict())

    return new_product_ref.key, 200

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