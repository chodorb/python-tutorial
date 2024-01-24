# Nazwe, producenta, cene, znizka?, ile_znizki?

class Product:   
    def __init__(self, name, producer, price, is_sale=False, sale_amount=0):
        self.name = name
        self.producer = producer
        self.price = price
        self.is_sale = is_sale
        self.sale_amount = sale_amount
        
    def get_price(self):
        if self.is_sale:
            return self.price - self.price * self.sale_amount
        else:
            return self.price
        
    def start_sale(self, sale_amount):
        self.is_sale = True
        self.sale_amount = sale_amount
        
    def stop_sale(self):
        self.is_sale = False
        
product1 = Product(name="PS5", producer="Sony", price=2500)
product1.start_sale(0.15)
print(product1.get_price())
product1.stop_sale()
print(product1.get_price())

