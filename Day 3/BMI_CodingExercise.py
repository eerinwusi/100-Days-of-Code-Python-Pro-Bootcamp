height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = int(weight) / (float(height) ** 2)

print(int(bmi))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")