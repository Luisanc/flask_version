from app import app
from flask import abort, request
from app.common.authentication import validate_token
from app.controllers.product_create import create_product
from app.models.product import Product

"""
Create a new product element

Required token: Bearer
Method: POST:
Argument: json body
{
    'sku': string,
    'name': string,
    'price': float,
    'brand': string,
    'stock': integer
}
Return: UUID(String)
"""
@app.route('/product/create', methods=['POST'])
def add_product():
    
    if not request.json:
        abort(400)        
    try:
        validate_token(request.authorization.token)
        
        new_product = Product(sku=request.json['sku'],
        name=request.json['name'],price=request.json['price'],
        brand=request.json['brand'],stock=request.json['stock'])
        
    except ValueError as e:
        return abort(403)
    
    return create_product(new_product)