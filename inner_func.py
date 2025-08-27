def hello(x):
    x()
    def world():
        print("inner hello")
        return 100
    return world
def u():
    print("params h")
print(hello(u)())
