class Gadget:
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price
    def __repr__(self):
        return f'{self.name} {self.brand} {self.price}'

class Mobile(Gadget):
    def __init__(self, name, brand, price,screen_size, ram):
        self.screen_size = screen_size
        self.ram = ram
        super().__init__(name, brand, price)
    def __repr__(self):
        return f'{super().__repr__()} {self.screen_size}  {self.ram}'

class Chip(Mobile):
    def __init__(self, name, brand, price, screen_size, ram, chip_name):
        self.chip_name = chip_name
        super().__init__(name, brand, price, screen_size, ram)

samsung = Mobile("a1","samsung",12000,5,12)
print(samsung)


