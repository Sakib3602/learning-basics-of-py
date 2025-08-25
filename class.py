"""
A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
every time in the class methonds we have to use self keyword as a default parameter must be used in the class methods.

"""

class phone :
    name = "samsung"
    model = "s20"
    color = "black"
    price = 50000

    def make_call(self,x):
        self.call = x
        return f'calling {self.call}...'

phone1 = phone()
print(phone1.name, phone1.model, phone1.color, phone1.price)
  
print(phone1.make_call("hello i am calling you"))