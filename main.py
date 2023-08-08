# - домашній номер телефону (тільки цифри та довжина номера)

import re
test_phone_number=["+123456","123456","q12345","12345","1234567"]#second number only true
true_phone_number= re.compile(r"^[\d]{6}$")#count numbers of phone number are 6

for phone_number in  test_phone_number :
    if true_phone_number.match(phone_number):
        print(f"phone number {phone_number}  true")
    else:
        print(f"phone number {phone_number}  wrong phone number")
print("Finish task 1")



# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
test_mobile_phone_number=["+123456789012","1234567890","12345678901",
                          "12345678901234","q1233","12345+123412"]
#first number and second number only true
# true_numbers= re.compile(r"^[+0-9]{1}\d{9,12}$")
for numbers in test_mobile_phone_number:
    if re.match(r"^[+]{1}\d{12}$",numbers):
        print(f"Mobile numbers  {numbers}  TRUE")
    elif re.match(r'^[0-9]{10}$',numbers):

        print(f"Mobile numbers  {numbers}  TRUE")
    else:
        print(f"Mobile numbers  {numbers}  false")
print("finish task 2")
# - email(наявність @, домену: gmail.com наприклад,
# мінімальна довжина та максимальна на ваш вибір)

test_email_adress=['_qwer@qwe.com','1qwe@qwe.com','1@qwqw.com','qwqe@1.com',
                   'qwqw@qwq.q','wqqwqwqw.com',
                   'qweertttyyyqweeddddddddddwsdwdwdwdwdwdwdwwyyy@jjj.keik']
true_email_adress= re.compile(r"^([0-9a-zA-Z._%+-]{2,36}@[0-9a-zA-Z]{2,}[.][a-zA-Z]{2,})$")
for email_adress in test_email_adress:
    if true_email_adress.match(email_adress):
        print(f"Email adres  {email_adress}  TRUE")
    else:
        print(f"Email adres  {email_adress}  false")
print("Finish task 3")
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
pib_test=['Igor Bondar Ievgenijovych','qwe qwqewer','q qwe qqwer',
          'qwertyuiopasdfghjklzqwe qwq wqew','1q dsde rff','AdsdsdSsdsAsd']

true_pib=re.compile(r'^[A-Za-z]{2,20}\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}$')
for pib in pib_test:
    if true_pib.match(pib):
        print(f"PIB  {pib}  TRUE")
    else:
        print(f"PIB  {pib}  false")
