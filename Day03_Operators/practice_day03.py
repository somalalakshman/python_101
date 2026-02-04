marks = int(input("Enter your marks: "))

if marks >= 65:
    print("first class")
elif marks >= 50:
    print("second class")
elif marks >= 35:
    print("third class")
else:
    print("Fail")





x = 20
y = 5

print ("sum", x+y )
print ("sub", x-y )
print ("mul", x*y )
print ("quo", x/y )
print ("mod", x%y )
print ("exp", x**y)





arjun_age = 24
karthik_age = 30

if arjun_age > karthik_age:
	print (" arjun_age is older")
elif karthik_age > arjun_age:
	print ("karthik_age is older")
else:
	print ("Both age are same ")
      




score = 50

score += 10
print ("after += ", score)
score -= 5
print("after -= ", score)
score *= 2
print("after *= ", score)
score /=3
print("after /=", score)



"""""
a = 30
b = 45

if a > b:
	print ("a is greater then b")
elif b < a:
	print ("b smaller then a")
elif a == b:
	print ("a equal to b")
else:
	print ("both are not equal")
	"""""


a = 30
b = 45

a = int(input("Enter first number :"))
b = int (input("enter second number: "))

if a > b:
	print ("a is greater then b")
elif b < a:
	print ("b smaller then a")
elif a == b:
	print ("a equal to b")
else:
	print ("both are not equal")


num1 = 20
num2 = 35

print ('sum', num1+num2)
print ('sub', num1-num2)
print ('mul', num1*num2)
print ('div', num1/num2)




"""
child_age = 13
teen_age = 13 <= 19
adult_age = 20 

if child_age  == int("child_age"):
	print ("child_age",)
elif teen_age = int("teen_age <= child_age ",):
	print ("teen_age")
elif adult_age = ("teen_age >= adult_age"):
else:
	print (adult_age)
"""

#SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='


age = int(input("Enter age: "))

if age < 13:
    print("Child")

elif 13 <= age <= 19:
    print("Teen")

else:
    print("Adult")





