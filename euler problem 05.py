#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 5.py

Copyright (c) 2013 . All rights reserved.

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num % value from range(1,21)

"""

#from sympy import *

def confirmmod(num):
	for i in range(2,21):
		if (num % i) != 0:
			#print(str(num) + "/" + str(i) + 'remainder')
			return True
	return False
			

def findnumber():
	x = 1
	while confirmmod(x):
	#while x < 2520:
	#	confirmmod(x)
		x += 1
	return x
	
print(findnumber())