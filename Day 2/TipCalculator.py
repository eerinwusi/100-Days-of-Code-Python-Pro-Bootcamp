print("Welcome to the tip calculator")

total_bill = input("What was the total bill? ")

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

total = (int(percentage_tip) / 100) * float(total_bill)

tentative_bill = float(total) + float(total_bill)

people = input("How many people to split the bill? ")

division = tentative_bill / int(people)

rounded_value = round(division, 2)

print(f"Each person should pay ${rounded_value}")