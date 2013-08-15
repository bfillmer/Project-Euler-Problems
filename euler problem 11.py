#!/usr/bin/env python
# encoding: utf-8
"""
euler problem 11.py

Copyright (c) 2013 . All rights reserved.

In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20x20 grid?

1. Figure out how to import as a set of sets
2. Process laterally (easy)
3. Rotate data 90 deg, process laterally (hard)
4. Create new sets from all diagonal sets > 4 in length (no clue). Process.

"""

#from sympy import *

# Grid Block as String
grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
# Test Case Grid
#grid = "1 2 3 4 5 6 7\n1 2 3 4 5 6 9\n1 2 3 4 5 89 7\n1 2 3 4 5 6 78"
# Number of Values to Multiply
nx = 4

# Function to return rows as lists within a master list.
def gridrows(grid):
	for row in grid.split("\n"):
		yield row.split(" ")

# Returns the products of all values in a row.
def rowvalues(nx,row):
	i = 0
	while i < (len(row)-(nx-1)):
		x = 0
		value = 1
		while x < nx:
			index = (i + x)
			value = value * int(row[index])
			x = (x + 1)
		i = (i + 1)
		yield value

def allrows(nx,grows):
	flist = []
	for row in grows:
		flist = flist + list(rowvalues(nx,row))
	yield flist

#grows = list(gridrows(grid))

#for row in grows:
#	print row

#allrows = list(allrows(nx,grows))
# Worked great, largest value returned not the final answer however.
#print(sorted(allrows[0]))

'''

Solution via Will Townes online. Same general solution method to what I wanted to do, but using quite a few
Python specific functions I do not know. Using for learing purposes.

In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20x20 grid?
'''

def prod(values):
    '''multiplies a list of numbers'''
    return reduce(lambda x,y:x*y,values)

def subproducts(matrix,n):
    '''finds the maximum horizontal, vertical, left diagonal ("\"), and right diagonal ("/") products
    of n adjacent values in a matrix.
    The matrix is a python list of lists (not numpy), and can have any dimensions.
    Clearly, n must be less than or equal to the smaller of the two matrix dimensions.'''
    #initialize all counters to zero.
    (horiz,vert,rdiag,ldiag) = tuple([0]*4) 
    rows = len(matrix)
    cols = len(matrix[0])
    assert n <= min(rows,cols)
    #find highest horizontal product:
    for i in range(rows):
        for j in range(cols-n):
            product = prod([grid[i][j+k] for k in range(n)])
            horiz = max(horiz,product)
            
    #find highest vertical product:
    for i in range(rows-n):
        for j in range(cols):
            product = prod([grid[i+k][j] for k in range(n)])
            vert = max(vert,product)
            
    #find highest "\" diagonal product:
    for i in range(rows-n):
        for j in range(cols-n):
            product = prod([grid[i+k][j+k] for k in range(n)])
            ldiag = max(ldiag,product)
            
    #find highest "/" diagonal product:
    for i in range(n-1,rows):
        for j in range(cols-n):
            product = prod([grid[i-k][j+k] for k in range(n)])
            rdiag = max(rdiag,product)
    return (horiz,vert,rdiag,ldiag)

if __name__ == "__main__":
    grid = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
    grid = grid.split('\n')
    for i in range(len(grid)):
        grid[i] = grid[i].split(' ')
        grid[i] = [int(grid[i][j]) for j in range(len(grid[i]))]
    #grid is now a list of lists, converted to integers
    champ = max(subproducts(grid,4))
    print(champ)
        
 