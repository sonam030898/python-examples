def greet_user():
    print('Hi there!!')
    print('This is a function')

print('Start')
greet_user()
print('Finish')

# function with parameters

def greet_user(name, lastName):
    print(f'Hi {name} {lastName}!!')
    print('This is a function')

print('Start')
greet_user("Sonam", "Jha")
greet_user("Mary", "JohnSon")
print('Finish')

# Square

def square(number):
    return number * number
    

print(square(3))