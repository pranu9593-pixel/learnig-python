# guess_game.py
import random
num = random.randint(1, 10)
guess = int(input("Guess the number between 1 and 10: "))
if guess == num:
    print("You guessed right!")
else:
    print(f"Wrong! The number was {num}")
