from random import *

print ("Hello there. What is your name?")
name = input()
name = name.lower()
name = name.capitalize()
print (("Well, %s, I am thinking of a number between 1 and 10.") % name)
x = randint(1, 10)
x = x
y = 1
guess = input()
guess = int(guess)
print (x)
print ("You have 5 guesses left.")
while y < 6:
    if guess == x:
        guess = str(guess)
        print(("Congratulations! You guessed %s. That is correct.") % guess)
        break
    elif guess > x:
        print("Sorry! You guessed too high. Please pick another number.")
        guess = input()
        guess = int(guess)
        y += 1
        z = str(y)
        print (("Guesses made: %s.") % z)
        continue
    elif guess < x:
        print("Sorry! You guessed too low. Please pick another number.")
        guess = input()
        guess = int(guess)
        y += 1
        z = str(y)
        print (("Guesses made: %s.") % z)
        continue
    else:
         print("That is not a number. Sorry.")


# break will break the loop. Continue will force the program to return to the start
# of the loop.  randint is imported from the random module.
# To import the number, I had to change it to a string str()
# for number of guesses made.
