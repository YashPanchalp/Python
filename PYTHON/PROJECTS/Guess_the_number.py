import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = 7

    print("************** WELCOME TO NUMBER GUESSING GAME *************")
    print("Guess the number between 1 and 100. You have 7 tries.")

    while attempts_left > 0:
        guess = int(input(f"You have {attempts_left} tries left. Enter your Guess or Quit(For Quit Enter 0) : "))

        if guess== 0:
            print("You Quit the Game ")
            break
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("<<<<<<<<<<<<Congrats! You guessed the number >>>>>>>>>>>>>>>")
            break

        attempts_left -= 1

    if attempts_left == 0:
        print(f"Sorry, the number was {number_to_guess}.")

guess_number_game()
