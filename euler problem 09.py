#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 9.py

Copyright (c) 2013 . All rights reserved.

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

1. Find partitions of 1000 that are comprised of three unique numbers.

"""

#from sympy import *

# Some code shamelessly stolen from online.
# Finds all partitions of k size in integer n.
def successor(n, l):
	idx = [j for j in range(len(l)) if l[j] < l[0]-1]
	if not idx:
		return False
	i = idx[0]
	l[1:i+1] = [l[i]+1]*(len(l[1:i+1]))
	l[0] = n - sum(l[1:])
	return True
	
# Some code shamelessly stolen from online.
# Finds all partitions of k size in integer n.
def partitions(n, k):
	l = [0]*k
	l[0] = n
	results = []
	results.append(list(l))
	while successor(n, l):
		results.append(list(l))
	return results

theparts = partitions(1000,3)

for i in theparts:
	c = i[0]
	b = i[1]
	a = i[2]
	if (a**2 + b**2) == c**2:
		print("a=" + str(a) + " b=" + str(b) + " c=" + str(c))
		print("a*b*c= " + str(a*b*c))

#print(partitions(1000,3))