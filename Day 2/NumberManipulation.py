# this rounds the result to a whole number
print(round(8 / 3))

# this specifies the amount of number after the decimal, in this case 2.
print(round(8 / 3, 2))

# this uses the concept of "floor" and makes it an integer without explicitly specifying conversion to integer
print(8 // 3)

score = 1
height = 1.8
isWinning = True

print("Your score is " + str(score) + ", " + str(height) + ", " + str(isWinning))
# instead of doing the above, you can use an f-String like below

# this is an f-String
print(f"Your score is {score}, your height is {height}, you're winning is {isWinning }")
