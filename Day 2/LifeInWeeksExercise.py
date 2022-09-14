# gets input of user's age
age = input("What is your current age? ")

# calculates amount of days, weeks, month,, years lived
years_left = 90 - int(age)
months_lived = int(age) * 12
weeks_lived = int(age) * 52
days_lived = int(age) * 365

months_left = int(1080.74 - months_lived)
weeks_left = int(4696.07 - weeks_lived)
days_left = int(32872.5 - days_lived)

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months")

print(int("5") * 2)