"""# strings in python
print ("python is fun")
print (''' "Quotes" and 'single quotes' can be tricky ''')

name = " Lakshman somala "
city = " Hyderabad "
age = 28

print (f"My name is {name} from {city} & iam {age}" )

# control statements in python
'''lift runing from 1st floor to 6 if we press 1 it will go to 1st floor 
and if we press 2 it will go to 2nd floor and so on'''

floor = int (input ("Enter the floor number: "))
if floor == 1:
    print ("Lift is going to 1st floor")    
elif floor == 2:
    print ("Lift is going to 2nd floor")
elif floor == 3:
    print ("Lift is going to 3rd floor")
elif floor == 4:
    print ("Lift is going to 4th floor")
elif floor == 5:
    print ("Lift is going to 5th floor")
elif floor == 6:
    print ("Lift is going to 6th floor")
elif floor == 0:
    print ("Lift is going to ground floor")

else:
    print ("Invalid floor number")


# Store and Print a Variable

name = "Lakshman somala"
age = 28
place = "Hyderabad"
print (f"Name: {name}, Age: {age}, Place: {place}")

#Take two numbers from user and print their data types.
num1 = 123
num2 = 77.82

print(type(num1))
print(type(num2))

#Create variables of different data types and print them.
name = "shanmuk"
age = 5
is_student = True
hight = 4.6
favorite_colour = ("red", "bule", "black")
number = [1,2,3,4,5,6,7]

print(name)
print(age)
print(is_student)
print(hight)
print(favorite_colour)
print(number)


print(type(name))
print(type(age))
print(type(is_student))
print(type(hight))
print(type(favorite_colour))
print(type(number))


#Take marks of 3 subjects and find average.
telugu = int(input("Enter marks: "))
English = int(input("Enter marks: "))
matchs = int(input("Enter marks: "))

average = (telugu + English + matchs)/3
print ("average", average)


#Store 5 numbers in a list and find the largest number.
number = [10, 20, 5, 30, 15]
largest = number[0]

for n in number:
    if n > largest:
        largest = n
print("The largest number is:", largest)

#Write a program to check if a number is even or odd.

num = int(input("Enter a Number: "))
if num % 2 == 0:
	print ("Even number")
else:
	print("Odd number")



num = int(input("Enter a number: "))
fact = 1

for i in range(1,num+1):
    fact = fact * i

print("Factorial =", fact)
"""


#Right Triangle Pattern

for i in range (1, 6):
	print ("*" * i)
	

n = 5
for i in range (1, n+1):
    print (" " * (n-i) + "*" * i)
    





  