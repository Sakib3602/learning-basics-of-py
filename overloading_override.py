print("=================Operator overLoading=================")
class hello:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return f'total {self.a + self.b + other.a + other.b}'
addi = hello(10,10)
addi2 = hello(11,11)

result = addi + addi2
print(result)

print("=================method override=================")

class Yo:
    def __init__(self):
        pass
    def helloPo(self):
        print("from Yo")
class honey(Yo):
    def helloPo(self):
        print("Yo honey")
di = honey()
di.helloPo()


        