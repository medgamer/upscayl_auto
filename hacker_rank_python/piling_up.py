
from collections import deque

def solve():
    _ = int(input())  # Number of cubes, not directly used in logic
    cubes = deque(map(int, input().split()))

    current_top = float('inf')  # Initialize with a very large value

    possible = True
    while cubes:
        if cubes[0] >= cubes[-1] and cubes[0] <= current_top:
            current_top = cubes.popleft()
        elif cubes[-1] <= current_top:
            current_top = cubes.pop()
        else:
            possible = False
            break

    if possible:
        print("Yes")
    else:
        print("No")

num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()

# Student average scores using zip

s = input()
n,x = [int(num) for num in s.split()]

st = list(range(1, n+1))

subs = []
for i in range(x):
    s = input()
    sub = [float(num) for num in s.split()]
    subs.append(sub)

z = zip(*subs)
for it in z:
    print(sum(it)/x)

# Check int and float using re and exceptions

import sys
import re

n = int(input())

for i in range(n):
    s = sys.stdin.readline()

    # Check int first
    if re.match(r"[-+]?\d+$", s) is not None:
        print(False)
    else:
        try:
            f = float(s)
            print(True)
        except:
            print(False)

# re.split large numbers

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# Use re to find substring

s = input()
k = input()

i = 0
su = s
while i<len(s)-len(k):
    ma = re.search(k, su)

    if ma:
        print(f"({ma.start()+i}, {ma.end()-1+i})")
        i += ma.start()+1
        su = s[i:]
    else:
        if i==0:
            print("(-1, -1)")
        break

# Use re to detect Roman numbers

import re

roman_numeral_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

def is_valid_roman_numeral(s):
    return bool(re.fullmatch(roman_numeral_pattern, s))

print(is_valid_roman_numeral("MCMXCIV"))  # True
print(is_valid_roman_numeral("MMXXV"))   # True
print(is_valid_roman_numeral("IIII"))    # False (invalid repetition)
print(is_valid_roman_numeral("VX"))      # False (invalid subtraction)

# Use re pattern to detect # hex colors in css ;-)

import re
import sys

regex = r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?(?!$)"

n = int(input())

test_str = ""
for i in range(n):
    s = sys.stdin.readline()
    if "{" in s:
        continue

    matches = re.findall(regex, s, re.MULTILINE)
    for cs in matches:
        print(cs)
