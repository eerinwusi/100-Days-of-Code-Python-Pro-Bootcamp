def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))

for operator in operations:
    print(operator)
input = input("Which of the operations do you want to do? ")

getter = operations[input]
answer = getter(num1, num2)

print(f"{answer}")