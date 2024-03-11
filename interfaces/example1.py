class Client:
    def __init__(self, first_name, last_name, money_spent=0.0, items_purchased=0, cart={"bike":500}, is_premium=False):
        self.first_name = first_name
        self.last_name = last_name
        self.money_spent = money_spent
        self.items_purchased = items_purchased
        self.cart = cart
        self.is_premium = is_premium
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __int__(self):
        return self.items_purchased
    
    def __float__(self):
        return self.money_spent
    
    def __bool__(self):
        return self.is_premium
    
    def __getitem__(self, key):
        return self.cart[key] 
    
    def __setitem__(self, key, value):
        self.cart[key] = value
    
    def __iter__(self):
        for key, value in self.cart.items():
            yield (key, value)

# __init__
c1 = Client("Bazyli", "Chodor")
c2 = Client("Janusz", "Kowalski")

# __str__
print(c1)
# __repr__
print([c1,c2])
# __int__
print(int(c1))
# __float__
print(float(c1))
# __bool__
print(bool(c1))
# __getitem__
print(c1["bike"])
# __setitem__
c1["gaming console"] = 500
c1["iphone"] = 1200
# __iter__
for product in c1:
    print(product)
