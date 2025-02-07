import random

def gamblingAddiction():                                            #Let's go gambling!
    global loss, found, name
    guess = int(input("Take a guess.\n"))
    if guess == theHouse:                                           #I just lost $300,000, but it's okay 'cause I won $700
        found = True
        print(f"Good job, {name}! You guessed my number in {loss} guesses! You are much better than 90% of gamblers who quit before they hit it big!")
    else:
        loss += 1                                                   #Aw dang it
        if guess < theHouse:
            print("Your guess is too low.")
        elif guess > theHouse:
            print("Your guess is too high.")

found = False
loss = 1
name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
theHouse = random.randrange(1, 21)                                  #The house sets a number 
while found == False:                                               #Lest you guess right, the house will drain you to the bone on repeat
    gamblingAddiction()

# EXAMPLE:
"""
Hello! What is your name?
Prower
Well, Prower, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Your guess is too low.
Take a guess.
19
Good job, Prower! You guessed my number in 4 guesses! You are much better than 90% of gamblers who quit before they hit it big!
"""
#god have mercy on tails