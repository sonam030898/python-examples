#while loops

i = 1
while i <= 5:
	print( ' * ' * i)
	i += 1 
print("Done")	

# for loops
for item in range(5,10, 2):
	print(item)


#Exercise
prices = [10, 20, 30]
total = 0
for item in prices:
	total += item
	print(f"Total: {total}")


#Nested Loops
for x in range(4):
	for y in range(3):
		print(f'({x}, {y})')

#Exercise
numbers = [2, 2, 2, 2, 7]
for x in numbers:
	#print('x' * x)  ---> easiest way 	
	output = ''
	for count in range(x):
		output += 'x'  
	print(output)





