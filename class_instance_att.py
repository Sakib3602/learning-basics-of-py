
"""
class attribute it shere all 
"""
class shop:
    cart = []
    def __init__(self,name):
        self.name = name
    def add_to_cart(self,item):
        self.cart.append(item)
mehjaben = shop("mehjaben")
mehjaben.add_to_cart("laptop")
mehjaben.add_to_cart("mobile")
print(mehjaben.cart)

niso = shop("niso")
niso.add_to_cart("shirt")
niso.add_to_cart("pant")
print(niso.cart)

"""instance attribute never share"""
print("-----instance attribute never share-----")
class SHOP:
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add_to_cart(self,item):
        self.cart.append(item)
sakib = SHOP("sakib")
sakib.add_to_cart("laptop")
sakib.add_to_cart("mobile")
print(sakib.cart)

rakin = SHOP("rakin")
rakin.add_to_cart("shirt")
rakin.add_to_cart("pant")
print(rakin.cart)