#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 15.py

Copyright (c) Bryan Fillmer 2013 . All rights reserved.

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Following code taken from Jason B. Hill's blog post on problem 15.
http://code.jasonbhill.com/python/project-euler-problem-15/

Thanks to his explanation of the problem and proof I'll attempt to write my own version of the 
code. Also working through his code below to garner some tricks for writing this type of 
looping in Python.

def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]

n = route_num(20)

Notes:

1. Loop through columns (for i) sum the current row values for the column (for j).
2. As we move left our increments for previous columns increase, using a multiple of
	2 to simulate having multiple directions as you would visually.

"""

# i,j both end up working on the same list values, which is how the summation adds up correctly
def latticeRoute(size):
	lattice = [1] * size # Create a list with size items
	for i in range(size): # Loop through all values 0 -> size
		for j in range(i): # Loop through all values 0 -> i
			lattice[j] = lattice[j] + lattice[j-1]
			# Set current lattice value = current value (1 for first row) + the previous value.
		lattice[i] = 2 * lattice[i - 1]
		# Set current lattice[i] to 2 * previous. This is due to the way the summation works as you
		# go down both 'sides' toward a value, left and downward.
	print lattice
	
latticeRoute(4)