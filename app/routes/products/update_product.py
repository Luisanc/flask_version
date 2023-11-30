from app import app
from flask import abort, request
from app.common.authentication import validate_token
from app.models.product import Product
from app.controllers.products_update import update_by_id

"""
Update product info by UUID

Required token: Bearer
Method: PUT:
Argument: path -> UUID
Return: Json
{
    'sku': string,
    'name': string,
    'price': float,
    'brand': string,
    'stock': integer
}
"""
@app.route('/product/update/<product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    
    if not request.json:
        abort(400)        
    try:
        validate_token(request.authorization.token)
        
        new_product = Product(sku=request.json['sku'],
        name=request.json['name'],price=request.json['price'],
        brand=request.json['brand'],stock=request.json['stock'])
        
    except ValueError as e:
        return abort(403)
        
    return update_by_id(product_id=product_id,product_item=new_product)