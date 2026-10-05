# Control Flow

# If-else
marks = 82
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

# For loop
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# While loop
count = 1
print("While loop:")
while count <= 5:
    print(count)
    count += 1

# Break and continue
print("Numbers skipping 3:")
for i in range(1, 11):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)
