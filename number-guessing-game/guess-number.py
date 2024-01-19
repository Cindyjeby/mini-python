#!/usr/bin/python3
import random

secret_num = random.randint(1, 50) #generates a random number from 1 to 50

attempts = 0 #number of guessed attempts
incorrect_attempts = 0
max_incorrect_attempts = 3

while True:
    guess = int(input("Enter your guess between (1-50): "))
    attempts += 1

    if guess == secret_num:
        print(f"Congratulations! You guessed {secret_num} in correctly in {attempts} attempts")
        attempts = 0
    elif guess < secret_num:
        print(f"Too low! retry")
    else:
        print(f"Too high! retry")

    #check for consecutive incorrect attempts then gives hint
    if guess != secret_num:
        incorrect_attempts += 1
        if incorrect_attempts == max_incorrect_attempts:
            print(f"\nHint: The number is between {secret_num - 10} and {secret_num + 10}")
        elif incorrect_attempts > max_incorrect_attempts:
            incorrect_attempts = 0

while True:
    play_number_guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break