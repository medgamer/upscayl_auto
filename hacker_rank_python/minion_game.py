def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

# Palindromic triangle solution using formula instead of str ;-)
for i in range(1,int(input())+1):
    print(((10**i - 1) // 9)**2)

n = int(input())

for i in range(n):
    s = input()
    a,b = s.split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print(f"Error Code: {e}")

from collections import namedtuple

Student = namedtuple('Student', 'ID MARKS NAME CLASS')


n = int(input())

s = input()
ra = s.split()
id = ra.index("MARKS")

sum = 0
for i in range(n):
    s = input()
    a = s.split()

    sum += int(a[id])

print(f"{sum/n:.2f}")

from datetime import datetime, timedelta

# Sun 10 May 2015 13:54:36 -0700
format_string = "%a %d %b %Y %H:%M:%S %z"

# Complete the time_delta function below.
def time_delta(t1, t2):

    d1 = datetime.strptime(t1, format_string)
    d2 = datetime.strptime(t2, format_string)

    df = d1 - d2

    return str(abs(df.days*24*3600 + df.seconds))

# Need to read raw string containing invalid \ ;-)
import sys
import re

n = int(input())

for i in range(n):
    s = sys.stdin.readline()
    try:
        re.compile(r"{}".format(s))
        print(True)
    except re.error:
        print(False)


if __name__ == '__main__':
    s = input()
    minion_game(s)
