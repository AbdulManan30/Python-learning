# Create a Guess Number Game
import random

n = random.randint(1, 100)
i = 0
guesses = 0
while i != n:  # loop until the user guesses the number
    i = int(input("Guess a number between 1 and 100: "))
    if n > i:
        print("Higher Number Please")
        guesses += 1

    elif n < i:
        print("Lower Number Please")
        guesses += 1
print("You guessed it in", guesses, "guesses", "The Number is ", n)
