#!/usr/bin/python3
import random

secret_num = random.randint(1, 50) #generates a random number from 1 to 50

attempts = 0 #number of guessed attempts

while True:
    guess = int(input("Enter your guess between (1-50): "))
    attempts += 1

    if guess == secret_num:
        print(f"Congratulations! You guessed {secret_num} in correctly in {attempts} attempts")
    elif guess < secret_num:
        print(f"Too low! retry")
    else:
        print(f"Too high! retry")