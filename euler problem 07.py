#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 7.py

Copyright (c) 2013 . All rights reserved.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""

from sympy import *

# Another cheesy sympy can do it for me. Could use the basic proof that a number is prime
# to write your own loop to test, keeping track of the number of the prime etc.
print(prime(10001))