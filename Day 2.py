# Tip Calculator
# Ask bill and tip, then add them and divide by total people and split the share for each

print("Welcome to the Tip Calculator")
bill = float(input("What was the Total bill? \n"))
tip = int(input("How much Tip would you like to give? 10%, 12% or 15%? \n"))
tip_percentage = (tip/100)*bill
split_the_bill = int(input("How many people do ypu want to split the bill? \n"))

each_ones_share = round((bill+tip_percentage)/split_the_bill,2)
print(f"Each person should pay: {each_ones_share}")