print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip_percentage / 100 + 1

pay = (bill * tip_as_percent) / people

print(f"Each person should pay: ${pay:.2f}") 
