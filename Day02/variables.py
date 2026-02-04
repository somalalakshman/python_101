
# string variable
# Concatenating strings
first_name = "Somala"
last_name = "Reddy"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# integer variable
age: int = 25

# float variable
height = 5.9

#boolean variable
is_student = True # snake case variable naming convention

print(full_name, age, height, is_student)

print("===========================  Variable Types  =========================")
# Use type() to check what kind of data is stored
print(type(full_name))     # str
print(type(age))      # int
print(type(height))   # float
print(type(is_student)) # bool

# Variables can be updated
age += 1 # 26
# which is equivalent to age = age + 1
print("Next year, age will be:", age)
