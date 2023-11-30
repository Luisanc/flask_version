from app import app
from app.controllers.products import get_all

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