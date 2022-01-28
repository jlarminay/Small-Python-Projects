# Leibniz Infinite Series
# By Joshuah Larminay
# Imports
import math
import os

# Variables
max = (10**100)
loop_total = 0
x = 0.0
real_pi = (math.pi)
pi = 0.0
p_error = 0.0

# Pre-Test Data
print("-----Leibniz Infinite Series-----\n")
print("max: \t\t", max)
print("loop_total: \t", loop_total)
print("x: \t\t", x)
print("real_pi: \t", real_pi)
print("pi: \t\t", pi)
print("p_error: \t", p_error)

input("\n\tNext: LOOP FUNCTION.")

# Loop Function
while pi != real_pi:

	os.system('cls')
	sigma = (4*(((-1)**( x ))/(((2)*( x ))+1)))
	pi += sigma
	
	print("-----Leibniz Infinite Series-----\n")
	print("Sigma: \t\t", sigma)
	print("Abs (Sigma): \t", (math.fabs(sigma)))
	print("\nActual: \t", real_pi)
	print("Generated: \t", pi)
	
	p_error = math.fabs((real_pi - pi) / real_pi)
	
	print("\n% Error: \t", p_error)
	x += 1
	loop_total += 1
	print("\nLoop = ", loop_total)

# End
input("\n\nEnter To Exit.")