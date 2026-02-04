# 🐍 Python Beginner Tutorial (Aligned with Your Plan)

## **Phase 1: Foundations**

### Lesson 1: Hello Python
```python
# Your first program
print("Hello, Somala! Welcome to Python.")
```
**Exercise:**  
- Change the message to greet yourself by name.  
- Try printing multiple lines using `\n`.

---

### Lesson 2: Variables & Data Types
```python
name = "Somala"
age = 25
height = 5.9
is_student = True

print(name, age, height, is_student)
```
**Exercise:**  
- Create variables for your favorite movie, year released, and rating.  
- Print them in a sentence like: *"My favorite movie is X, released in Y, rated Z."*

---

### Lesson 3: Input & Output
```python
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello", user_name, "you are", user_age, "years old!")
```
**Exercise:**  
- Ask the user for two numbers and print their sum.  

---

## **Phase 2: Control Flow**

### Lesson 4: Conditionals
```python
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```
**Exercise:**  
- Write a program that asks for a score and prints “Pass” if ≥ 50, otherwise “Fail”.

---

### Lesson 5: Loops
```python
for i in range(1, 6):
    print("Iteration:", i)
```
**Exercise:**  
- Print the multiplication table of 7.  
- Write a loop that counts down from 10 to 1.

---

## **Phase 3: Data Structures**

### Lesson 6: Lists & Dictionaries
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # prints apple

contacts = {"Alice": "1234", "Bob": "5678"}
print(contacts["Alice"])
```
**Exercise:**  
- Add a new fruit to the list.  
- Create a dictionary of 3 friends with their favorite colors.  

---

## **Phase 4: Functions & Modular Programming**

### Lesson 7: Functions
```python
def greet(name):
    return "Hello, " + name

print(greet("Somala"))
```
**Exercise:**  
- Write a function that takes two numbers and returns their product.  

---

### Lesson 8: Modules
```python
import random

print(random.randint(1, 10))  # random number between 1 and 10
```
**Exercise:**  
- Use the `math` module to calculate the square root of 144.  

---

## **Phase 5: Practical Projects**

### Mini Project: Number Guessing Game
```python
import random

secret = random.randint(1, 10)
guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("You guessed it!")
else:
    print("Wrong! The number was", secret)
```
**Exercise:**  
- Modify the game to give the user 3 chances.  

---

### Mini Project: To-Do List
```python
tasks = []

while True:
    task = input("Enter a task (or 'quit' to stop): ")
    if task == "quit":
        break
    tasks.append(task)

print("Your tasks:", tasks)
```
**Exercise:**  
- Save tasks to a file using `open("tasks.txt", "w")`.  

---

## ✅ How to Use This Tutorial
- Work through **one lesson per day**.  
- After each lesson, **modify the code** to make it personal (e.g., change names, numbers, or add features).  
- Keep all your scripts in a folder — you’ll see your progress grow week by week.  

---

Would you like me to **expand this into a week-by-week calendar** (like “Day 1: Hello Python, Day 2: Variables…”), so you can follow it like a structured course?
