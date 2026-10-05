# Collections and Loops

# List
numbers = [1, 2, 3, 4, 5]
print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# List operations
numbers.append(6)
print("After append:", numbers)
print("Length:", len(numbers))

# Tuple
point = (10, 20)
print("Tuple:", point)

# Set
letters = {"a", "b", "a", "c"}
print("Set:", letters)  # duplicates removed

# Dictionary
student = {"name": "Sara", "age": 22, "course": "Python"}
print("Dictionary:", student)
print(student["name"])

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)
