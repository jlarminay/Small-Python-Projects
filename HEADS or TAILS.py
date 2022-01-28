import random
import time
import os

money = 30
goal = 1000
options = (["heads", "tails"])

print ("-----------------------------------------")
print "-------------HEADS and TAILS-------------"
print "-----------------------------------------"
print "\nYour goal is to reach", goal, "dollars by betting"
print "money on what side the coin will land on."

raw_input("\nPress ENTER to start.")

while ( 0 < money < goal ):
	os.system('cls')
	print "-----------------------------------------"
	print "-------------HEADS and TAILS-------------"
	print "-----------------------------------------"
	print "\n*****-You have", money, "dollars left-*****"
	print "Your Guess:\t"
	print "You Wager:\t"
	time.sleep(0.5)
	
	coin = random.choice(options)

	guess = raw_input("\nWhat is your guess?: ")
	while (guess != "heads") and (guess != "tails") and (guess != "h") and (guess != "t"):
		print "\nThats not a proper choice."
		print "Please pick again."
		guess = raw_input("\nWhat is your guess?: ")
		
	if guess == "heads" or guess == "h":
		guess = "heads"
	elif guess == "tails" or guess == "t":
		guess = "tails"
	else:
		print "ERROR"
		raw_input("\nPress ENTER to start.")
		
	
	os.system('cls')
	print "-----------------------------------------"
	print "-------------HEADS and TAILS-------------"
	print "-----------------------------------------"
	print "\n*****-You have", money, "dollars left-*****"
	print "Your Guess:\t", guess
	print "You Wager:\t"
	time.sleep(1.0)
	
	bet = int(raw_input("\nHow much do you wager?: "))
	while (bet < 0) or (bet >= money + 1):
		if bet < 0:
			print "You can't bet a negative number."
		elif bet > money:
			print "You can't bet more than you have."
		bet = int(raw_input("\nHow much do you wager?: "))
	
	os.system('cls')
	print "-----------------------------------------"
	print "-------------HEADS and TAILS-------------"
	print "-----------------------------------------"
	print "\n*****-You have", money, "dollars left-*****"
	print "Your Guess:\t", guess
	print "You Wager:\t", bet
	time.sleep(1.0)
	
	print "\nNow to flip the coin."
	time.sleep(0.5)	
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
	print "-----------------------------------------"
	print "-------------HEADS and TAILS-------------"
	print "-----------------------------------------"
	print "\n*****-You have", money, "dollars left-*****"
	print "Your Guess:\t", guess
	print "You Wager:\t", bet

	print "\n\nThe coin is", coin

	if guess == coin:
		print "\nYou guessed right!"
		print "You won", bet, "dollars!"
		money = money + bet
	else:
		print "\nYou guessed wrong."
		print "You lost", bet, "dollars."
		money = money - bet
		
	time.sleep(3.5)	
	
os.system('cls')
print "-----------------------------------------"
print "-------------HEADS and TAILS-------------"
print "-----------------------------------------"

if money <= 0:
	print "\nYou are out of money."
	time.sleep(0.9)
	print "\n\n\t-------------------"
	print "\t-----GAME OVER-----"
	print "\t-------------------"
elif money >= 100:
	print "\nYou have reached your goal."
	time.sleep(0.9)
	print "\n\n\t-----------------"
	print "\t-----YOU WIN-----"
	print "\t-----------------"
else:
	print "\nERROR"


raw_input("\n\nPress the enter key to exit.")
