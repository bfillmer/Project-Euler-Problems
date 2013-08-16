#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 14.py

Copyright (c) Bryan Fillmer 2013 . All rights reserved.

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Bryan's notes:

1. Love Collatz Conjecture!
2. Would be nice to know terms in the sequence without computing.
3. Research on Wikipedia: can throw out powers of 2, 2^n, as they would always reduce "quickly" n times.
Pause
4. Have brute force chain generation. Now to loop to one million, store chain length, and get the longest one.
"""

#from sympy import *

# Loop to find all numbers in the sequence for any given number n. Tag on a one for printing purposes.
"""
def collatzLoop(n):
	while n != 1:
		yield n
		n = collatzCheck(n)
	yield 1
"""

# Modified loop to store chain length. Add one for the one.
def collatzLoop(n):
	l = 0
	while n != 1:
		n = collatzCheck(n)
		l = l + 1
	l = l + 1
	return l

# Actual logic of the Collatz Conjecture.	
def collatzCheck(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3*n + 1

# Loop through all numbers 1 to 1 million, getting chain lengths. Compare then, store the current largest chain
# and the number that started it all.
def megaLoop():
	largestChain = 1, 1
	for i in range(1,1000001):
		c = collatzLoop(i)
		if c > largestChain[1]:
			largestChain = i, c
	return largestChain
	
print megaLoop()