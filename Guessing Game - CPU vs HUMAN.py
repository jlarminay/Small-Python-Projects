# Computer VS. Human

import random
import time
import os

max_number = 1000
top = max_number
min_number = 0
bot = min_number

p_tries = 1
c_tries = 1

print "------------------------------------------"
print "-----------Number Guessing Game-----------"
print "--------------CPU vs. HUMAN---------------"
print "------------------------------------------"
print "\nYou can pick a number between ", min_number, "and ", max_number
print "I will try to guess it in as little guesses as possible."
print "I will then pick a number and you must guess it as I did."
print "Whoever guesses the number in as little guesses wins."

raw_input("\nPress ENTER to start.")

os.system('cls')
print "------------------------------------------"
print "-----------Number Guessing Game-----------"
print "--------------CPU vs. HUMAN---------------"
print "------------------------------------------"

print "\nYou can start when ready."

p_number = int(raw_input("\n>> "))

while (p_number > max_number -1 or p_number < min_number +1):
	print "Invalid Choice"
	print "Please Enter Another Number"
	p_number = int(raw_input("\n>> "))


os.system('cls')
print "------------------------------------------"
print "-----------Number Guessing Game-----------"
print "--------------CPU vs. HUMAN---------------"
print "------------------------------------------"

# Computer Guessing Turn	
	
c_guess = (top+bot)/2
	
while (c_guess != p_number):
	if c_guess > p_number:
		print "\nYour number: \t", p_number
		print "I guess:\t", c_guess
		print "Lower."
		top = c_guess
	elif c_guess < p_number:
		print "\nYour number: \t", p_number
		print "I guess:\t", c_guess
		print "Higher."
		bot = c_guess
	else:
		print "END-------------------"

	c_guess = (top+bot)/2
	c_tries += 1
	time.sleep(2.0)
	
	os.system('cls')
	print "------------------------------------------"
	print "-----------Number Guessing Game-----------"
	print "--------------CPU vs. HUMAN---------------"
	print "------------------------------------------"
	
print "\n--I guessed your number--"
print "Your number was", p_number
print "\n\nNow its your turn to try and beat me."

time.sleep(2)
c_number = int(random.randrange(max_number) +1)
print "I have chosen my number. You may now begin guessing."
time.sleep(3)

# Player Guessing Turn

os.system('cls')
print "------------------------------------------"
print "-----------Number Guessing Game-----------"
print "--------------CPU vs. HUMAN---------------"
print "------------------------------------------"

p_guess = int(raw_input("\nTake a guess: "))

while (p_guess != c_number):
	if(p_guess > max_number):
		print "That's higher than the max..."
	elif(p_guess < min_number):
		print "It can't be less than zero."
	elif(p_guess > c_number):
		print "Lower."
	else:
		print "Higher."

	p_guess = int(raw_input("\nTake a guess: "))
	p_tries += 1
	
os.system('cls')
print "------------------------------------------"
print "-----------Number Guessing Game-----------"
print "--------------CPU vs. HUMAN---------------"
print "------------------------------------------"

print "\n--You guessed my number--"
print "My number was", c_number

print "\n\nNow to compare tries."

# Score
time.sleep(1.0)
print "."
time.sleep(0.5)
print ".."
time.sleep(0.5)
print "..."
time.sleep(0.5)
print "...."
time.sleep(0.5)
print "....."
time.sleep(0.5)

os.system('cls')
print "------------------------------------------"
print "-----------Number Guessing Game-----------"
print "--------------CPU vs. HUMAN---------------"
print "------------------------------------------"

if p_tries < c_tries:
	print "\n\t*****!!YOU WIN!!*****"
	print "It only took you", p_tries, "tries and it took me", c_tries, "tries."
elif p_tries > c_tries:
	print "\n\t*****!!I WIN!!*****"
	print "It only took me", c_tries, "tries and it took you", p_tries, "tries."
elif p_tries == c_tries:
	print "\n\t*****!!IT'S A TIE!!*****"
	print "It took us both", c_tries, "tries."
else:
	print "DIE------"

raw_input("\n\nEnter To Exit")