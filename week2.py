# Jovanny Rosado
# Number guessing game
from random import randint
answer = randint(1, 100)
guess = -1
while guess != answer:
    print ("Enter your guess:") 
    guess = input()
    guess = int(guess)
    if guess > answer:
        print("Too High")
    elif guess < answer :
        print ("Too Low")
print ("You figured it out")
