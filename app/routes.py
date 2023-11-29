from app import app
from flask import abort, jsonify, request
from app.common.authentication import validate_token, authenticate_user
from app.controllers.products import create_product, get_by_id, delete_by_id, update_by_id, get_all
from app.models.product import Product

@app.route('/')
def index():
    return 'Welcome to the Catalog System!'

@app.route('/login', methods=['POST'])
def login():
    if not request.json or 'email' not in request.json or 'password' not in request.json:
        abort(400)  # Bad request if required fields are missing

    email = request.json['email']
    password = request.json['password']
    
    return authenticate_user(email=email, password=password)
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

"""
Get all products info

Method: GET:
Return: Json
{
    "UUID":{
        'sku': string,
        'name': string,
        'price': float,
        'brand': string,
        'stock': integer
    }   
}
"""
@app.route('/products', methods=['GET'])
def get_all_products():
    return get_all()
    