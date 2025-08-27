from abc import ABC,abstractmethod
class hello:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def op(self):
        pass # only declaration
    def __repr__(self):
        return f'{self.name} :::: {self.age}'
    
class World(hello):
    def op(self): # must use
        print("Abstract method")
    def __init__(self, name, age,ho):
        self.ho = ho
        super().__init__(name, age)
    def __repr__(self):
        return f'{super().__repr__()} ::: {self.ho}'

ui = World("dogi",23,"opopo")
print(ui)
    
