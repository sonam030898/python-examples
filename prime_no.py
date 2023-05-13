# Check number is prime or not

# num = int(input('Enter the number: '))

# if num == 1:
#     print(num, 'is not a prime number')
# elif num > 1:
#     if num % 2 == 0:
#         print(num, ' is not a prime number')
#     else:
#         print(num, ' is a prime number')


# Print all the prime numbers in one interval

lower = 3
higher = 98

print("Prime numbers between", lower, "and", higher, "are:")

for num in range(lower, higher +1):
    if num > 1:
        for i in range(2, num):
            if num % 2 == 0:
                break
        else:
            print(num)