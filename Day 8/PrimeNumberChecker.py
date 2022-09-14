def prime_checker(number):
    if number == 2 or number == 3:
        print("It's a prime number")
    elif number % 2 == 0 or number % 3 == 0:
        print("It's not a prime number")
    else:
        print("It's a prime number")

# Another implementation
def prime_checker1(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_Prime = False
    if is_Prime == False:
        print("It's not a prime number")
    else:
        print("It's a prime number")

n = int(input("Check this number: "))
prime_checker1(n)

