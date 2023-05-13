number = int(input('Enter the number: '))

factorial = 1

# check if number is negative or number is valid or not

if number < 0:
    print('Uhhhh,,, Sorry please enter valid number!!!!')
elif number == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, number +1):
        factorial *= i
    print(f'The factorial of {number} is {factorial}')