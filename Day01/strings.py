# String operations in Python
# String practice

s = "Lakshman"

s = s + " Somala"
print(s)
# s=s+10 # TypeError: can only concatenate str (not "int") to str
# Note: String can only be concatenated with another string

# s=+ " 10" #TypeError: bad operand type for unary +: 'str'

s = s + " 10"  # Correct way to concatenate string with number as string

s = s + """ completed MBA in 2022. 
He has good experience in aws, pythong jenkins
He born in Mudibugga viallage"""


print(s)