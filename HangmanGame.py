import time
import random

name = input("What is your name? ")

print("Hello, " + name + " Time to play hangman!")
time.sleep(1)

print("Start guessing...\n")
time.sleep(0.5)


words = ['python', 'programming', 'treasure', 'creative', 'medium', 'horror']

word = random.choice(words)

guesses = ''
turns = 5

while turns > 0:

    failed = 0

    
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1

    print()

    
    if failed == 0:
        print("You won")
        print("The word was:", word)
        break

    
    guess = input("guess a character: ")

    guesses += guess

    
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, "more guesses")

        if turns == 0:
            print("You lost")
            print("The word was:", word)
