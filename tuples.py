# tuples are like list but list means => [] & tuples => ()
numbers = (1, 2, 3)
# We can't chnge value of tuples. It is immutable
print(numbers[0])

# UNPACKING

coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# short-hand property for above 9-10lines code.
x, y, z = coordinates  # this is unpacking

print(x)