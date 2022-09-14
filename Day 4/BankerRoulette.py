import random

names_string = input("Give me everybody's names, seperated by a comma ")

names = names_string.split(", ")

bill_payer = random.randint(0, len(names) - 1)

print(f"{names[bill_payer]} will pay the bills.")