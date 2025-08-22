def no():
    a = int(input("Enter a number: "))
    print("You entered:", type(a), a)
no()
b= 0
print("Before:", b)
def condition():
    b = input("Enter a character: ")
    if b == "rahim":
        print("You entered rahim")
    elif b== "siam":
        print("You entered siam")
    elif b == "sakib":
        print("You entered sakib")
    elif b == "sabbir":
        print("You entered sabbir")
    else : 
        print("You entered something else")
condition()
# deafult value 0 no error will give
def sum (num1, num2, num3=0):
    t = num1 + num2 + num3
    return t
print("Sum is:", sum(10, 20))


"""
error will give
def sum (num1, num2, num3):
    t = num1 + num2 + num3
    return t
print("Sum is:", sum(10, 20))

"""

