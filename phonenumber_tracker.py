import phonenumbers
from phonenumbers import carrier, geocoder, timezone

x = phonenumbers.parse('+918779137226', None)
print(x)

mobile = input("Enter the phone number: ")
mobileNo = phonenumbers.parse(mobile)

# 
print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, 'en'))

print(geocoder.description_for_number(mobileNo, 'en'))

print("Valid Mobile Number: ", phonenumbers.is_valid_number(mobileNo))

print("Check possibility of Mobile Number: ", phonenumbers.is_possible_number(mobileNo))