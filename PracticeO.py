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

if sakib > musfiq and sakib > kamal and sakib > jack and sakib > kalam:
    print("Sakib is older")
elif musfiq > sakib and musfiq > kamal and musfiq > jack and musfiq > kalam:
    print("Musfiq is older")
elif kamal > sakib and kamal > musfiq and kamal > jack and kamal > kalam:
    print("Kamal is older")
elif jack > sakib and jack > musfiq and jack > kamal and jack > kalam:
    print("Jack is older")
elif kalam > sakib and kalam > musfiq and kalam > jack and kalam > kamal:
    print("Kalam is older")


# this will also work
# Find the oldest cricketer
# oldest = max(sakib, musfiq, kamal, jack, kalam)
# print(f"{oldest.name} is the oldest")