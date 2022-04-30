
# If-else conditions
is_hot = False
is_cold = False
if is_hot:
	print("It's hot day")
	print('Drink Plenty of water')
elif is_cold:
	print("It's a cold day")
	print('Wear warm clothes')
else:
	print("It's a lovely day")
print('Enjoy your Day')

#Exercise
house_price = 1000000
good_credit = False
if good_credit:
	down_payment = 0.1 * house_price
else: 
	down_payment = 0.2 * house_price
print(f"Down Payment: ${down_payment}")

# Logical Conditions => and , or, not

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
	print("Eligible for Loan")


has_good_credit = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
	print("Eligible for Loan")


#Comparison Operators
temperature = 30
if temperature != 30: 
	print("It's hot day")
else: 
	print("It's cold day")
	

#Exercise
name = "Jvvvv"
if len(name) < 3: 
	print('Name must be atleast 3 characters long')
elif len(name) > 50:
	print('Name must be max 50 characters long')
else: 
	print('Name looks good')









