# Pizza Delivery using Conditional Statements

print("Welcome to Pizza Delivery!")
size = input("How many sizes would you like? S,M or L? \n ")
pepperoni = input("Do you want pepperoni? Y or N? \n ")
cheese = input("Do you want cheese? Y or N \n ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Sorry, please enter S, M, or L")

if pepperoni == "Y":
    if size == "S":
        bill +=2
    elif size == "M" or size == "L":
        bill +=3
else:
    print("Sorry, please enter Y or N")

if cheese == "Y":
    bill += 3
else:
    print("Sorry, please enter Y or N")

print(f"Your total bill is: ${bill}.")