num = input('Enter the number: ')

reverse = 0
# Using while loop
# while num!=0:
#     digit = int(num) % 10
#     reverse = reverse*10 + digit
#     num = int(num)//10

# print("Reversed number: " +  str(reverse))


# Using string slicing
print("Number before reversing: " + num)

# [::-1] -->> [start:stop:step] ==>> when step is -1 the start goes to end and stop at front.
print(str(num)[::-1]) 