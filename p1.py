# Kate Archer
# CSCI 3038
# Project 1
# June 2, 2016

import sys      # Imports the necessary
import random     # modules for the program.
import math

#random.seed(0)     # Seed for de-bugging purposes

numDarts = int(sys.argv[1])   # Sets the number of darts from the argument list.

inCircle = 0      # Accumulator for darts in the circle.
radius = 1      # Established radius for comparison.

for i in range(numDarts): # For loop for dart throwing.
  x = random.random()
  y = random.random()
  disFromCenter = math.sqrt(x*x + y*y)
  if (disFromCenter <= radius):   # Determines if in the circle and
    inCircle += 1     # updates accumulator.

piEstimate = 4 * (float(inCircle / numDarts)) # Calculates pi estimate.

print("pi estimate = ", piEstimate)   # Prints result.
