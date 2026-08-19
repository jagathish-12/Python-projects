# Tip Calculator
print("Welcome to the Tip Calculator")
bill = float(input("What was the Total bill? \n"))
tip = int(input("How much Tip would you like to give? 10, 12 or 15? \n"))
split_the_bill = int(input("How many people do ypu want to split the bill? \n"))

each_ones_share = round((bill+tip)/split_the_bill,2)
print(f"Each person should pay: {each_ones_share}")