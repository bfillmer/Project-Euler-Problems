#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 4.py

Copyright (c) 2013 . All rights reserved.

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Thoughts:

Start by multiplying largest three digit numbers and descending, stop when
encountering a palindrome.

First attempt: 999 * 999 -> 100, print results.

Issues:

How the heck to check for a palindrome.
	Theory: Take value, use function to reverse, subtract. Should be zero.
"""

from sympy import *

# Generate the list of numbers of 999 * 999 -> 2.
def generatenumbers():
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			num = j*i
			if checkpalindrome(num):
				yield num

# Reverse integer via converstion to string and back.
def reverse_int(n):
   return int(str(n)[::-1])

# Check that the number is a palindrome. Only return if is.
def checkpalindrome(num):
	r = reverse_int(num)
	if (r-num) == 0:
		return True

#print(list(generatenumbers()))
#print(list(checkpalindrome(909)))

print(list(sorted(generatenumbers())))