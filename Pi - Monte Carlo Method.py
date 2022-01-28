# Monte Carlo Method
# By Joshuah Larminay
# Imports
import math
import random
import os

# Variables
max = 10**100
loop_total = 0
add = 0.0
M = 0.0
N = 0.0
real_pi = (math.pi)
pi = 0.0
p_error = 0.0

# Pre-Test Data
print "-----Monte Carlo Method-----\n"
print "max: \t\t", max
print "loop_total: \t", loop_total
print "add: \t\t", add
print "M: \t\t", M
print "N: \t\t", N
print "real_pi: \t", real_pi
print "pi: \t\t", pi
print "p_error: \t", p_error

raw_input("\n\tNext: LOOP FUNCTION.")

# Loop Function
while pi != real_pi:

	os.system('cls')

	print "-----Monte Carlo Method-----"
	
	x = random.random()
	y = random.random()

	print "\n(", x, ",", y, ")"	
	add = (x**2) + (y**2)
	print "add: \t", add
	if add <= 1:
		M += 1
		N += 1
		print "\nM:", M
		print "N:", N
	elif add > 1:
		N += 1
		print "\nM:", M
		print "N:", N
	else:
		raw_input("\n\nERROR DETECTED")
	
	loop_total += 1
	
	print "\nActual: \t", real_pi
	pi = (4.0* M) / N
	print "Generated: \t", pi
	
	p_error = math.fabs((real_pi - pi) / real_pi)
	
	print "\n% Error: \t", p_error
	
	print "\nLoop: \t", loop_total

print "\n\nTotal M:", M
print "Total N:", N

pi = (4.0* M) / N

print "\n", pi

# End
raw_input("\n\nEnter To Exit.")