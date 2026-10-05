# Functions and Scope

# Function with parameters

def add(a, b):
    return a + b


print(add(5, 7))

# Function with default parameter

def greet(name="User"):
    return f"Hello, {name}!"


print(greet())
print(greet("Rahim"))

# Local vs global scope

global_value = 100


def update_global():
    global global_value
    global_value += 20
    print("Inside function:", global_value)


update_global()
print("Outside function:", global_value)

# Returning multiple values

def calculate(a, b):
    return a + b, a - b, a * b


sum_value, diff, product = calculate(10, 5)
print(sum_value, diff, product)
