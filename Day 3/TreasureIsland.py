print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

decision = input("left of right? ").lower()

if decision == "right":
    print("Game over")
elif decision == "left":
    decision1 = input("swin or wait? ").lower()
    if decision1 == "swim":
        print("Game Over")
    else:
        decision2 = input("Which door? ").lower()
        if decision2 == "red":
            print("Game over")
        elif decision2 == "blue":
            print("Game over")
        elif decision2 == "yellow":
            print("You win!")