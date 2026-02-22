# Python number guessing game
import random

lowest_num = 0
highest_num = 1
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while True:
    while is_running:

        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print("That number is out of range")
                print(f"Select a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too low! Try again!")
            elif guess > answer:
                print("Too high! Try again!")
            else:
                print(f"CORRECT! The answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False
        else:
            print("Invalid guess")
            print(f"Select a number between {lowest_num} and {highest_num}")

    while True:
        again = input("Do you want to play again? (y/n): ").lower()
        if again == "y":
            is_running = True
            break
        else:
            is_running = False
