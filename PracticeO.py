class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    def __gt__(self,other):
        return self.age > other.age
        

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 40, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 227, 68, 95)

if sakib > musfiq and kamal and jack and kalam:
    print("sakib is older")
elif musfiq > sakib and kamal and jack and kalam:
    print("Musfic is older")
elif kamal > sakib and musfiq and jack and kalam:
    print("kamal is older")
elif jack > sakib and musfiq and kamal and kalam:
    print("Jack is older")
elif kalam > sakib and musfiq and jack and kamal:
    print("kalam is older")
