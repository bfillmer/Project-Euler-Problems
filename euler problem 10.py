#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 10.py

Copyright (c) 2013 . All rights reserved.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from sympy import *

answer = 0
for i in sieve.primerange(1, 2000000):
	answer = answer + i
	
print(answer)