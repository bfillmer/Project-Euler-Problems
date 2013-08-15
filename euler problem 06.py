#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 6.py

Copyright (c) 2013 . All rights reserved.

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

"""

#from sympy import *

def generatesquares():
	for i in range(1,101):
		yield i**2
		
#print(sum(list(generatesquares())))

#print(sum(range(1,11))**2)

print("(Sum of Squares - Square of Sums) of n <= 100: ")
print((sum(range(1,101))**2)-(sum(list(generatesquares()))))