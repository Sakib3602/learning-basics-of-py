def hello(num1,num2):
    sum = num1 + num2
    mult = num1 * num2
    rem = num1 % num2
    # return [sum, mult, rem]  # Returning a list (not recommended for multiple return values)
    return sum, mult, rem  # Returning multiple values as a tuple

x = hello(10, 20) # This will print the tuple (30, 200, 10)

sum, mult, rem = hello(10, 20) # Unpacking the returned tuple into separate variables
print("Sum:", sum)
print("Multiplication:", mult)
print("Remainder:", rem)

for i in x:
    print(i)



