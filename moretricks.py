#!/usr/bin/env python3

# Use Of Ternary Operator For Conditional
# Assignment.

def small(a, b, c):
	return a if a <= b and a <= c else (b if b <= a and b <= c else c)
	
print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

vector = [m**2 if m > 10 else m**4 for m in range(50)]
print(vector)

#Multi-line strings
multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)

multiStr = """select * from multi_row 
where row_id < 5"""
print(multiStr)

multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age") 
print(multiStr)

# Dictionary/Set Comprehensions.
testDict = {i: i * i for i in range(10)} 
testSet = {i * 2 for i in range(10)}

print(testSet)
print(testDict)

# inspect object in python3
test = [1, 3, 5, 7]
print( dir(test) )

# Detect Python Version At Runtime.

import sys

#Detect the Python version currently in use.
    
if not sys.version_info >= (3,5):
    print("Sorry, you aren't running on Python 3.5\n")
    print("Please upgrade to 3.5.\n")
    sys.exit(1)

#Print Python version in a readable format.
print("Current Python version: ", sys.version)
