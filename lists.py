names = ['John', 'Bob', 'Mosh', 'Sonam', 'Marry']
print(names[:])
names[0] = "Jon"
print(names)

#Excersise ---> Largest number

numbers = [3,10, 6, 9, 2, 0, 4, 1]
max = numbers[0]
for number in numbers:
	if number > max:
		max = number
print(max)

# 2D lists
matrix = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
print(matrix[0][1])

for row in matrix:
	for item in row:
		print(item)

# list methods
numbers = [3,10, 6, 9, 2, 0, 4, 1]
numbers.append(20)
print(numbers)
numbers.insert(0, 12)
print(numbers)  
# numbers.clear()  
# print(numbers)
numbers.pop()
print(numbers)
print(50 in numbers)
print(numbers.count(0))
numbers.sort()
numbers.reverse()
num = numbers.copy()
numbers.append(10)
print(numbers)
print(num)


# Excersise ---> Remove duplicates 

numbers = [2,2,4,6,2,5,1]
unique = []

for number in numbers:
	if number not in unique:
		unique.append(number)
print(unique)