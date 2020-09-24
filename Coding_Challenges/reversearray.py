"""
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .

Reverse an array of integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Function Description
Complete the function reverseArray in the editor below.
reverseArray has the following parameter(s):
N i.e. length of array A.
int A[n]: the array to reverse
Returns
int[n]: the reversed array
Input Format
The first line contains an integer, , the number of integers in .
The second line contains  space-separated integers that make up .

Constraints
"""

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):

    new_list = []
    count = 0
    while len(new_list) < len(a):
        for i in a:
            count +=1
            new_list.append(a[len(a)-count])
    #         count += 1
            # print(new_list)

    return new_list



a = [1, 3, 4, 2]
print(reverseArray(a))
