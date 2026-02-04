"""You are traveling from Hyderabad to Anantapur, distance is 600 kms.
you need 500 liters of fuel for the trip.
Ask user for current fuel in the vehicle (in liters).
If fuel is sufficient, print "You can start your journey"
If fuel is insufficient, print "You need X more liters to start your journey"
"""


"""fuel_needed_travel = 500
user_current_fuel_input = input("Enter current fuel in the vehicle: ")
current_fuel = int(user_current_fuel_input)

is_fuel_sufficent = fuel_needed_travel < current_fuel


if is_fuel_sufficent:
	print("You can start your journey")

else:
	fuel_required  = fuel_needed_travel - current_fuel
	print(f"you need {fuel_required} more liters to start journey")

"""
	

# string variable Practice

first_name = "somala" 
middle_name = "lakshman"
last_name = "choudhary"
full_name = (f"{first_name} {middle_name} {last_name}")
print("Full Name:", full_name)



""" 
   - Create variables for your favorite movie, year released, and rating.  
   - Print them in a sentence like:  
     `"My favorite movie is X, released in Y, rated Z."`
     """


#program:-

movie_name = "Simhadri"
released_year = 2003
moive_rating = 3.5
print (f"My favorite movie is {movie_name}, released in {released_year}, rated {moive_rating}.")



"""2. **Math Practice**  
   - Store two numbers in variables.  
   - Print their sum, difference, product, and quotient.
   """

#program:-

a = 25
b = 5

print("sum", a+b)
print("sub", a-b)
print("mul", a*b)
print("div", a/b)



"""3. **Boolean Fun**  
   - Create a variable `is_raining = False`.  
   - Print `"Take an umbrella"` if it’s True, otherwise `"Enjoy the sunshine"`.
   """

#program:-

is_raining = input("is_raning? (True/False): ")
if is_raining:
	print("Take an umbrella")
else:
	print("Enjoy the sunshine")


"""4. **Challenge**  
   - Write a script that asks the user for their name and age, then prints:  
     `"Hello Somala, you are 25 years old!"` (replace with actual input).
"""
#program:-

name = input("Enter your name")
age = input("Enter your age")

print (f"Hello {name}, you are {age}, years old!")





name = "Somala Lakshman Choudhary"
date_of_birth = 13,11,1997
age = 22
college = "sri sai jr college" 
print (f"name: {name}, date_of_birth: {date_of_birth}, age: {age}, college: {college}!")




full_name = "raja"
age = 30
height = 5.5
is_student = True

print(type(full_name))
print(type(age))
print(type(height))
print(type(is_student))



lunch_start = 12
lnch_end = 13

tea_start = 16
tea_end = 17

ct = input("Enter currnt timeee? ")
cur_time = int(ct)

if cur_time > 12 and cur_time < 13:
	print("It's a lunch time")
elif cur_time > 16 and cur_time < 17:
	print("It's a tea time")
else:
	print("Go practice python")














