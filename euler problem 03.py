#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 3.py

Copyright (c) 2013 . All rights reserved.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from sympy import *

# This one is kind of cheating as sympy has a prime factorization library.
print(primefactors(600851475143))