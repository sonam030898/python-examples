######################### using simple iteration #########################
# num = int(input('Enter the number: '))
# temp = num
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = (reverse * 10) + digit
#     temp = temp // 10
# print(reverse, num)
# if num == reverse:
#     print('Palindrome')
# else:
#     print('Not Palindrome')
    

    
# ################### palindrome using reversed built-in function #################### #
def checkPalindrome(str):
    # using inbuilt reversed function
    reverse = ''.join(reversed(str))

    if str == reverse:
        return True

    return False


# main function
s = "kayak"

print('Palindrom') if checkPalindrome(s) else print('no Palindrome')