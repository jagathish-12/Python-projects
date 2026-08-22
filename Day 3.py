# Roller Coaster using conditional statements

print("Welcome to Roller Coaster Ride.")
height = int(input("What is your height in cm? \n"))

bill = 0

if height >= 120:
    print("You can ride the ride")
    age = int(input("What is your age? \n"))
    if age <= 12:
        bill = 5
        print("you are a child.")
    elif age <= 18:
        bill = 10
        print("you are a teenager.")
    elif age < 45:
        bill = 15
        print("you are a adult.")
    elif age <= 55:
        bill = 0
    else:
        print('Please enter correct age')

    photo = input("Do you want a photo? (y/n) \n")
    if photo == "y":
        bill += 3
    else:
        print("Sorry, please enter y or n")

    print(f"The total bill is, ${bill}.")
else:
    print("You can't ride the ride")

