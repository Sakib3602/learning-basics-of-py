class Animal:
    def __init__(self,name,breed,price):
        self.name = name
        self._breed = breed
        self.__price = price  # private
    def __repr__(self):
         return f"Animal(name={self.name}, breed={self._breed}, price={self.__price})" 
class YoAni(Animal):
    def __init__(self, name, breed, price,pol):
        self.pol = pol
        super().__init__(name, breed, price)
    def __repr__(self):
        return f'{super().__repr__()} ++ {self.pol}'
    

dog = YoAni("dog","british",20000,222)

dog._breed = "bangali"  # protected it can be change
dog.name = "kutta"  # public thats why change
print(dog)
print(dog._breed)
print(dog.name)

# print(dog.__price)    # This is is private thats why it will not work.

