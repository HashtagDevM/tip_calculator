print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to give? 10, 12 0r 15? "))
people = int(input("How many people to split the bill? "))
portion_payable = bill * (tip / 10) / people
total = "{:.2f}".format(portion_payable)
print(f"Each person should pay: ${total}")