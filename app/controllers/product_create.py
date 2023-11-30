from firebase_admin import db
from app.models.product import Product

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