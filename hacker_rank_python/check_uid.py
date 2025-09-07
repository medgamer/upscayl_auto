
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

def is_valid(s:str)->str:
    if len(s)!=10:
        return "Invalid"
    if not s.isalnum():
        return "Invalid"

    counter = Counter()
    na = 0
    nd = 0
    for c in s:
        if c.isdigit():
            nd +=1
        elif c.isupper():
            na +=1
        counter += Counter({c : 1})

    if na<2 or nd<3:
        return "Invalid"

    # Check duplicate chars
    for c in counter:
        if counter[c]>1:
            return "Invalid"

    # Finally after passing all conditions ;-)
    return "Valid"


n = int(input())

for i in range(n):
    s = input()
    print(is_valid(s))


# Use re to check credit card numbers ;-)

import re

def is_valid_credit(s:str)->str:
    if len(s)==19 and s[4]=='-' and s[9]=='-' and s[14]=='-':
        s = s[0:4]+ s[5:9] + s[10:14] + s[15:]

    if len(s)!=16 or (not s.isdigit()):
        return "Invalid"

    if int(s[0])<4 or int(s[0])>6:
        return "Invalid"

    matches = re.findall(r'(\d)(\1*)', s)

    for digit, repeats in matches:
        if len(repeats)>=3:
            return "Invalid"

    return "Valid"

# Use regex for postal codes

import re

regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(?=(\d)\d\1)'	# Do not delete 'r'.

# res = re.findall(regex_alternating_repetitive_digit_pair, "110000")
# print(res)


import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Matrix script solution : difficult one

#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List, Dict

def matrix_to_str(mat:List[str], n:int, m:int)->str:
    s = ""
    for j in range(m):
        for i in range(n):
            s += mat[i][j]
    return s

# Use regex to format ms as correct output str.
def str_re_format(ms: str)->str:
    return re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', ms)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

ms = matrix_to_str(matrix, n, m)
fs = str_re_format(ms)

print(fs)
