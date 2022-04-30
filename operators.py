# Arithmetic Operators
print(10+3)
print(11 // 3)
print(11 % 3)

# Assignment Operators
x = 3
# instead of writing in this way
#x = x + 5
# use this syntax
# This operator is known as Augmented Assignment Operator
x += 5
print(x)
y = 15
y -= 3
print(y)

# Operator Precedance

x = 10 % 2 + 5 ** 3 - 10
print(x)

# Order of Precedance =>  i.) Paranthesis & thn  Exponential(2 ** 3) 
#	        	  ii.) Muliplication & Division
#			 iii.) Addition & Substraction

x = (2 + 3) * 10 - 3 
print(x)
