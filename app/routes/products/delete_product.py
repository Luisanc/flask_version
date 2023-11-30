from app import app
from flask import abort, request
from app.common.authentication import validate_token
from app.controllers.product_delete import delete_by_id

"""
Remove product

Required token: Bearer
Method: DELETE:
Argument: path -> UUID
Return: Message includes UUID (String)
"""
@app.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product_by_id(product_id):
    try:
        validate_token(request.authorization.token)
        
    except ValueError as e:
        return abort(403)
        
    return delete_by_id(product_id=product_id)