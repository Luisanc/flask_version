class Product:
    def __init__(self, sku, name, price, brand, stock):
        self.sku = sku
        self.name = name
        self.price = price
        self.brand = brand
        self.stock = stock

    def to_dict(self):
        return {
            'sku': self.sku,
            'name': self.name,
            'price': self.price,
            'brand': self.brand,
            'stock': self.stock
        }

    def is_valid(self):
        # Validatation of datatypes
        if not (isinstance(self.sku,str) and 
        isinstance(self.brand,str) and 
        isinstance(self.name,str) and 
        (isinstance(self.price,float) and self.price >=0) and 
        (isinstance(self.stock,int) and self.stock >=0)):
            return False
        
        return True