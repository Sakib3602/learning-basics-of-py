
xx = int(input("Enter a number: "))
class Calculator:
    def __init__(self, name, price):
        self.penPrice = xx
        self.name = name
        self.price = price

    def x(self):  
        if self.price > self.penPrice:
            change = self.price - self.penPrice
            return f'back taka {change}'
        elif self.price == self.penPrice:
            return f'Thank you for buying anything else you need?'
        else:
            need = self.penPrice - self.price
            return f'need more {need} taka.'

matador = Calculator("matador", 69)
print(matador.x())
