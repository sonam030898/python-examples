# Only unique keys are allowed
customer = {
    "name" : "sonam jha",
    "age" : 30,
    "email" : "sonam@gmail.com",
}

print(customer["name"])

# Excercise

phone = input("Phone ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
}
output = ''

for char in phone:
    output += digits_mapping.get(char, "!") + " "
print(output)

# Emoji Converter

message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "🙂",
    ":(" : "😞",
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)
