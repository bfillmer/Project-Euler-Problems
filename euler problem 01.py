#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 1.py

Created by Bryan Fillmer on 2013-06-18.
Copyright (c) 2013 . All rights reserved.
"""

def check(rng):
	sum = 0
	for x in rng:
		if (x%3 == 0) or (x%5 == 0):
			sum = sum + x
	return sum
		
#print(list(check(range(0, 1000))))
print(check(range(0,1000)))