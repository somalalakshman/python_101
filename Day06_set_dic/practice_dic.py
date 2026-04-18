# Creating a dictionary in different methods
# method 1

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

# dictionary with data
my_dict = {
    "name": "Lakshman",
    "age": 25,
    "city": "Hyderabad"
}

print(my_dict)

student = {
    "name": "Raja",
    "age": 22,
    "courses": ["Math", "Science", "History"]
}
print(student)

# method 2 using dict() constructor
person = dict(name="lakshman", age=22, city="hyderabad")
print(person)

# method 3 using  list of tuples
person_info = [("name", "lakshman"), ("age", 22), ("course", "python"),("city", "hyderabad")]
print(dict(person_info))
