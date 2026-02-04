""" units = int(input("Enter units consumed: "))
if units <= 100:
    bill_amount = units * 2
elif units <= 200:
    bill_amount = (100 * 2) + (units - 100) * 3
elif units <= 300:
    bill_amount = (100 * 2) + (100 * 3) + (units - 200) * 5  
else:
    print("total bill amount is:", )
    


units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Total bill amount: ₹", bill)



# Check positive or negative

num = int(input ("Enter a number:"))

if num > 0:
	print ("positive")
else:
	print ("Negative")




#Login system (real-time example)


user_name = input("Enter username: ")
password = input ("Enter password: ")

if user_name == ("admin") and password == ("606765"):
	print ("Login sucessfull")
else:
	print ("invalid user_name or password")
	

# Traffic  signal  system

signal = input ("Enter signal colour: ")

if signal == ("red"):
	print ("Stop")
elif signal == ("green"):
	print ("Go")
elif signal == ("Yellow"):
	print ("wailt")
else:
	print ("invalid signal")
    


# Age-based ticket price

age = int(input("Enter age:"))

if age < 5:
	print ("Ticket is free",)
elif age <= 12:
	print ("child ticket")
elif age >= 18 and age < 60:
	print ("adult ticket")
else:
	print ("senior citizen ticket")



#Basic calculator 

num1 = int(input("Enter 1st number:"))
oper = input ("Enter the operator (+,-,*,/): ")
num2 = int(input("enter 2nd number:"))

if oper == '+':
	print(num1 + num2)
elif oper == '-':
	print (num1 - num2)
elif oper == '*':
	print (num1 * num2)
elif oper == '/':
	print (num1 / num2)
else:
	print ("invalid operator")"""



# ATM withdrawal check

balance = 5000
amount = int(input("Enter withdraw amount:"))

if amount <= balance:
	print ("collect cash")
	print("Remaining balance:", balance - amount)
else:
	print ("Insufficient balance")






