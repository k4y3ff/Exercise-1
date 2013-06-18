import random

name = raw_input("Hey! What's your name? ")

print "So, %s, we're going to play a game." % name
print "I'm thinking of a number between 1 and 100. Try to guess a number."

random_number = random.randrange(1, 101)

print random_number

player = int(raw_input("What number are you thinking of? "))


while player != random_number:

	if player < random_number:
		print "Your guess is too low."
	else:
		print "Your guess is too high."

	player = int(raw_input("What number are you thinking of? "))

print "Congratulations! You've guessed correctly."
