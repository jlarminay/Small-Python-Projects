import random
import os
import time

#EXPLINATIONS
r_s     = "Rock crushes Scissors."
r_l     = "Rock crushes Lizard."
p_r     = "Paper covers Rock."
p_sp    = "Paper disproves Spock."
s_p     = "Scissors cut Paper."
s_l     = "Scissors decapitate Lizard."
l_sp    = "Lizard poisons Spock."
l_p     = "Lizard eats Paper."
sp_s    = "Spock smashes Scissors."
sp_r    = "Spock vaporizes Rock."

p_win = "Player Wins."
c_win = "Computer Wins."
tie = "Its a Tie."

p_score = 0
c_score = 0
t_score = 0
rounds = 0

#START

print "----------------------------------------"
print "----Rock.Paper.Scissors.Lizard.Spock----"
print "----------------------------------------"

rounds = int(raw_input("\nHow many rounds?: "))

while (((rounds%2) == 0) or (rounds <= -1)):
        print "It has to be a odd number and higher than 0."
        rounds = int(raw_input("\nHow many rounds?: "))


t_rounds = rounds

os.system('cls')        
print "----------------------------------------"
print "----Rock.Paper.Scissors.Lizard.Spock----"
print "----------------------------------------"
print "\n", rounds, "rounds left."

        
while (((t_rounds/2+1) > p_score) and ((t_rounds/2+1) > c_score)):

        poss = (["rock", "paper", "scissors", "lizard", "spock"])

        c_choice = random.choice(poss)
        p_choice_L = raw_input("\n\nYour Choice: ")
        p_choice = p_choice_L.lower()

        while ((p_choice != poss[0]) and (p_choice != poss[1]) and (p_choice != poss[2]) and (p_choice != poss[3]) and (p_choice != poss[4])):
                print "\nThat's not a proper choice."
                print "Please pick again."
                p_choice_L = raw_input("\n\nYour Choice:")
                p_choice = p_choice_L.lower()
                

        os.system('cls')        
        print "----------------------------------------"
        print "----Rock.Paper.Scissors.Lizard.Spock----"
        print "----------------------------------------"
        print "\n", rounds, "rounds left."

        print "\n\nPlayer's Choice:\t", p_choice
        print "Computer's Choice:\t", c_choice
        print "\n"      
        rounds -= 1
        time.sleep(1.0)

        #WINNER
        #p_win
        if ((p_choice == poss[0]) and (c_choice == poss[2])):
                print p_win
                print r_s
                p_score += 1
        elif ((p_choice == poss[0]) and (c_choice == poss[3])):
                print p_win
                print r_l
                p_score += 1
        elif ((p_choice == poss[1]) and (c_choice == poss[0])):
                print p_win
                print p_r
                p_score += 1
        elif ((p_choice == poss[1]) and (c_choice == poss[4])):
                print p_win
                print p_sp
                p_score += 1
        elif ((p_choice == poss[2]) and (c_choice == poss[1])):
                print p_win
                print s_p
                p_score += 1
        elif ((p_choice == poss[2]) and (c_choice == poss[3])):
                print p_win
                print s_l
                p_score += 1
        elif ((p_choice == poss[3]) and (c_choice == poss[4])):
                print p_win
                print l_sp
                p_score += 1
        elif ((p_choice == poss[3]) and (c_choice == poss[1])):
                print p_win
                print l_p
                p_score += 1
        elif ((p_choice == poss[4]) and (c_choice == poss[2])):
                print p_win
                print sp_s
                p_score += 1
        elif ((p_choice == poss[4]) and (c_choice == poss[0])):
                print p_win
                print sp_r
                p_score += 1
        #c_win
        elif ((p_choice == poss[2]) and (c_choice == poss[0])):
                print c_win
                print r_s
                c_score += 1
        elif ((p_choice == poss[3]) and (c_choice == poss[0])):
                print c_win
                print r_l
                c_score += 1
        elif ((p_choice == poss[0]) and (c_choice == poss[1])):
                print c_win
                print p_r
                c_score += 1
        elif ((p_choice == poss[4]) and (c_choice == poss[1])):
                print c_win
                print p_sp
                c_score += 1
        elif ((p_choice == poss[1]) and (c_choice == poss[2])):
                print c_win
                print s_p
                c_score += 1
        elif ((p_choice == poss[3]) and (c_choice == poss[2])):
                print c_win
                print s_l
                c_score += 1
        elif ((p_choice == poss[4]) and (c_choice == poss[3])):
                print c_win
                print l_sp
                c_score += 1
        elif ((p_choice == poss[1]) and (c_choice == poss[3])):
                print c_win
                print l_p
                c_score += 1
        elif ((p_choice == poss[2]) and (c_choice == poss[4])):
                print c_win
                print sp_s
                c_score += 1
        elif ((p_choice == poss[0]) and (c_choice == poss[4])):
                print c_win
                print sp_r
                c_score += 1
        #other
        elif ((p_choice == c_choice)):
                print tie
                t_score += 1
                rounds += 1
        else:
                print "ERROR ERROR ERROR ERROR"
        time.sleep(2.0)

        raw_input("\nPress Any Key To Continue.")
        
        os.system('cls')
        
        print "----------------------------------------"
        print "----Rock.Paper.Scissors.Lizard.Spock----"
        print "----------------------------------------"
        
        if (((t_rounds/2+1) > p_score) and ((t_rounds/2+1) > c_score)):
                print "\n", rounds, "rounds left."
        else:
                print ""
        
                

print "\n\nNow to calculate the winner."

print "\n."
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
        
print "----------------------------------------"
print "----Rock.Paper.Scissors.Lizard.Spock----"
print "----------------------------------------"

if p_score > c_score:
        print "\nThe Player Wins!"
        print "The player scored", p_score, "out of", t_rounds, "round(s)."
        print "The computer only scored:", c_score
elif c_score > p_score:
        print "\nThe Computer Wins!"
        print "The computer scored", c_score, "out of", t_rounds, "round(s)."
        print "The player only scored:", p_score
else:
        print "\nIts a Tie!"
        print "The player and computer both scored", p_score, "out of", t_rounds, "round(s)."

raw_input("\n\nEnter To Exit.")
