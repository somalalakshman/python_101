fruits =  ["apple", "banana", "cherry", "121", "raja"]
for e in fruits:
    print("I like ", e)



for i in range(1, 10):
    print(i)

for n in range (5):
	print("I love india")

print("**********")

for n in range (1,6,1):
	print(n)	
print("**********")

for n in range (1,11,1):
	print(2*n)
print("**********")


for n in range (1,11,1):
	print(2,"*",n,"=",2*n)

print("**********")

for ch in "Python":
    print(ch)

print("**********")

# number (1,2,3,4,5)
# find the maximum number in a list


numbers = (1,2,3,4,5)

max_num = numbers[0]

for num in numbers:
	if num > max_num:
		max_num = num
	
print ("maximum number is:",max_num)

print("**********")

for n in range (1,11,1):
	print (3,"*",n,"=",3*n )



i = 1
while i <= 5:
    print(i)
    i += 1



#Sum of first n numbers
n = int(input("Enter n: "))
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)



print ("python is fun")
print (''' "Quotes" and 'single quotes' can be tricky ''')

name = " Lakshman somala "
city = " Hyderabad "
age = 28

print (f"My name is {name} from {city} & iam {age}" )





