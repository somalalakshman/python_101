"""

## **Exercises**

1. **Personal Info Script**  
   - Create variables for your favorite movie, year released, and rating.  
   - Print them in a sentence like:  
     `"My favorite movie is X, released in Y, rated Z."`
"""
movie_name =  "Devara"
year_released = 2024
rating = 5.0

print(movie_name, year_released, rating)


"""
2. **Math Practice**  
   - Store two numbers in variables.  
   - Print their sum, difference, product, and quotient.
"""
a = 20
b = 30
print("sum:", a+b)
print("sub",a-b)
print("mul",a*b)
print("div",a/b)


"""
3. **Boolean Fun**  
   - Create a variable `is_raining = False`.  
   - Print `"Take an umbrella"` if it’s True, otherwise `"Enjoy the sunshine"`.
"""
# Control flow with boolean
is_raining = input("is_raining? (True/False): ")
if is_raining:
    print("Take an umbrella")
else:
    print("Enjoy the sunshine")


"""
4. **Challenge**  
   - Write a script that asks the user for their name and age, then prints:  
     `"Hello Somala, you are 25 years old!"` (replace with actual input).
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + ", you are " + age + " years old!")
# Alternatively, using f-strings
print(f"Hello {name}, you are {age} years old!")


"""balance
ask customer for withdraw amount
print remaining balance

Rules:
- if withdraw amount is greater than balance, print "Insufficient funds"
"""

bank_bal = 2000
withdraw_amount = input("enter withdraw amount:")
if int(withdraw_amount) > bank_bal:
    print("Insufficient funds. Your balance is:", bank_bal)
else:
    remaining_bal = bank_bal - int(withdraw_amount)
    print(f"Remaining bal: {remaining_bal}") 

