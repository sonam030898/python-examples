
# For 's we wrap the string with " "
course = "Python's for Beginners"
print(course) 

# For highlighting a word with " " wrap the string with ' '
course = 'Python for "Beginners"'
print(course) 

# If want the text in email or paragraph wrap the string with ''' '''
course = '''
Hi John,

How are you??

Thanks and Regards,
Sonam Jha

'''
print(course) 

# Characteristics of Strings
course = 'Python for Beginners'
#	  012345 678 9......
another_var = course[:]
print(course[0])
print(course[-1])
# It will print from 0 to 2, it will exclude the 3rd index
print(course[0:3])
# If we don't pass 2nd index then it will return the whole string
print(course[0:])
# If we dont pass any value then it will return the whole string because 1st index consider bydefault as (0) and 2nd index it will consider the whole length of the string and return the whole text.
print(another_var)

# exercise
name = 'Jennifer'
print(name[1:-1])

#Formatted string
first_name = 'Sonam'
last_name = 'Jha'
# f => formatted string
message = f'{first_name} [{last_name}] is a coder'
print(message)

# Strings Method
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course)
print(course.lower())
# find() method is case sensitive
print(course.find('B'))
print(course.replace('o', 'p'))
print('python' in course)

# Note: Diff betn find() and 'in' operator is find() returns the index and in-operator produces the boolean value















