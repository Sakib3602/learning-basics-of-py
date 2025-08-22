# ---------------------- Example 1: *args ----------------------

# A function that accepts unlimited arguments using *arg
def all_sum(*arg):  
    # All arguments are collected into a tuple
    print(arg)  
    return arg  

# Here we call the function and check the return type (it will always be tuple)
print("args", type(all_sum(10, 20, 30, 40, 50)))  

# Printing the actual tuple returned by the function
print("args", all_sum(10, 20, 30, 40, 50))  

# Looping through the returned tuple and printing each element
for c in all_sum(10, 20, 30, 40, 50):
    print(c)


# ---------------------- Example 2: Global variable ----------------------

# A global variable (outside the function)
xx = 0  

# Function with required argument (num1), optional argument (num2), and *arg for unlimited numbers
def all_sum_d(num1, num2=0, *arg):   
    global xx   # Allow function to use and modify the global variable 'xx'
    for i in arg:
        xx += i   # Add each extra argument to global variable 'xx'
    return num1 + num2 + xx   # Return the sum of all values

# Example call
print("args", all_sum_d(10, 20, 30, 40, 50))  


# ---------------------- Example 3: **kwargs ----------------------

# Function with normal argument (first) and **args for unlimited keyword arguments
def famous_name(first, **args):
    # Printing first argument
    print("First name:", first)  
    
    # Looping through keyword arguments (dictionary form)
    for key, value in args.items():
        print(f"{key}: {value}")  

# Example call (extra data is passed as key=value)
famous_name("Sakib", last="Al Hasan", age=35, team="Bangladesh")
