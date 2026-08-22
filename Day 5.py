# Treasure island game
from random import choice

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice_1 = input("Right or Left? ").lower()
if choice_1 == "right":
    print("Fall into a hole.\nGame over")
elif choice_1 == "left":
    choice_2 = input("Swim or wait? ").lower()
    if choice_2 == "swim":
        print("Attacked by trout.\nGame over")
    elif choice_2 == "wait":
        choice_3 = input("Red or Blue or Yellow? ").lower()
        if choice_3 == "red":
            print("Burned by fire.\nGame over")
        elif choice_3 == "blue":
            print("Eaten by beasts.\nGame over")
        elif choice_3 == "yellow":
            print("You win!")
        else:
            print("Please enter either 'Red' or 'Blue' or 'Yellow'")
    else:
        print("please enter either 'Swim' or 'Wait'")
else:
    print("Please enter Right or Left.")