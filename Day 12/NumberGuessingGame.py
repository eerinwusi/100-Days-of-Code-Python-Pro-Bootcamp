
# prompt user for input for easy or hard
# if user chooses easy, give them 10 attempts else if user chooses hard, give them 5 attempts
# create a variable that stores a random number
# prompt user for a number
# compare user input with the random number
# if user input is greater than random number, print too high
# else if user input is less than random number print too low
# else if user input is equal to random number, print you got it and end game
# keep prompting user for input until the user has exhausted number of guesses
import random

print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")

user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
while user_choice != "easy" and user_choice != "hard":
    user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1, 100)
play_game = True

while play_game == True:
    if user_choice == "easy":
        number_of_guesses = 5
        print(f"You have {number_of_guesses} attempts to guess the number")
        while number_of_guesses > 0:
            user_input = input("Guess a number: ")
            if int(user_input) > random_number:
                print("Too high")
                number_of_guesses -= 1
                print(f"You have {number_of_guesses} more attempt(s).")
            elif int(user_input) < random_number:
                print("Too low")
                number_of_guesses -= 1
                print(f"You have {number_of_guesses} more attempt(s).")
            else:
                print("You got it")
                break
            if number_of_guesses == 0:
                print("You didn't get the number, try again.")
        user_wants_to_play_again = input("Do you want to play again. Type 'y' or 'n': ")
        if user_wants_to_play_again == 'n':
            play_game = False

    else:
        number_of_guesses = 10
        print(f"You have {number_of_guesses} attempts to guess the number")
        while number_of_guesses > 0:
            user_input = input("Guess a number: ")
            if int(user_input) > random_number:
                print("Too high")
                number_of_guesses -= 1
                print(f"You have {number_of_guesses} more attempt(s).")
            elif int(user_input) < random_number:
                print("Too low")
                number_of_guesses -= 1
                print(f"You have {number_of_guesses} more attempt(s).")
            else:
                print("You got it")
                break
            if number_of_guesses == 0:
                print("You didn't get the number, try again.")
        user_wants_to_play_again = input("Do you want to play again. Type 'y' or 'n': ")
        if user_wants_to_play_again == 'n':
            play_game = False

