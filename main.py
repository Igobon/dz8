# - домашній номер телефону (тільки цифри та довжина номера)
#count numbers of phone number are 6
import re
test_phone_number=["+123456","123456","q12345","12345","1234567"]
true_phone_number= re.compile(r"^[\d]{6}$")

for phone_number in  test_phone_number :
    if true_phone_number.match(phone_number):
        print(f"phone number{phone_number} true")
    else:
        print(f"phone number{phone_number}wrong phone number")
