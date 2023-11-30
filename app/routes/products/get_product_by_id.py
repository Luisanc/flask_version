from app import app
from flask import abort, request
from app.common.authentication import validate_token
from app.controllers.product_get_one import get_by_id

"""
Get product info by UUID

Required token: Bearer
Method: GET:
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
@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    
    try:
        validate_token(request.authorization.token)
        
    except ValueError as e:
        return abort(403)
        
    return get_by_id(product_id=product_id)