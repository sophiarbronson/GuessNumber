#s.bronson 9/5/19

import random
#Random number chosen by the computer
number=random.randint(1, 100)
guess=0


guess=int(input("Guess a number between 1 and 100: "))

if guess != number:
	while(guess != number):
		if guess > number:
			print ("Guess is too high")
			guess=int(input("Guess again: "))
		elif guess < number:
			print ("Guess is too low")
			guess=int(input("Guess again: "))
		else:
			print "That was not an option, Goodbye."
			exit()
elif guess == number:
	print ("Correct! Good job!")
else:
	print ("That was not an option, Goodbye.")

print ("Correct! Good job!")
