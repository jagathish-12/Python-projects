# Password Generator

import random
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*']

number_of_alphabets = int(input("Enter the number of alphabets: "))
number_of_symbols = int(input("Enter the number of symbols: "))
number_of_numbers = int(input("Enter the number of numbers: "))

length = number_of_numbers + number_of_symbols + number_of_alphabets

if length >= 8:
    password = []
    for i in range(0,number_of_alphabets):
        password.append(random.choice(alphabets))
    for i in range(0,number_of_symbols):
        password.append(random.choice(symbols))
    for i in range(0,number_of_numbers):
        password.append(random.choice(numbers))

    final_password = ""
    # print(f"before : {password}")
    # random.shuffle(password)
    # old_password = password
    # print(f"After : {old_password}")

    for passwords in password:
        final_password += passwords

    print(f"Your password is : {final_password}")
else:
    print("Please enter a number greater than 8")






