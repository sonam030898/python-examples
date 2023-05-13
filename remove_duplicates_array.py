# Remove duplicates from sorted array

sorted_array = [0,0,0,1,1,2,3,3,4,5,6,6,6,7,7,7,8,8]

unique_array = []

for i in sorted_array:
    if i not in unique_array:
        unique_array.append(i)
    # return unique_array
print(unique_array)