
import numpy as np

np.set_printoptions(legacy='1.13')

# Get one line input of numbers as string and split into list
s = input()
int_list = [int(num) for num in s.split()]

# Use map(int, s.split())
integer_list = list(map(int, input().split()))

s = input()
f_list = [float(num) for num in s.split()]

# Get input numpr array of n lines each m int
s = input()
n,m = [int(num) for num in s.split()]

ar = np.zeros((n,m), dtype = int)

for i in range(n):
    s = input()
    ar[i] = [int(num) for num in s.split()]

# Custom sort
dm = {
    '1' : '0',
    '3' : '1',
    '5' : '2',
    '7' : '3',
    '9' : '4',
    '0' : '5',
    '2' : '6',
    '4' : '7',
    '6' : '8',
    '8' : '9'
}

# Compare 2 char by lower, upper, odd, even weird order ;-)
def myfunc(a):
    at = 0 if a.islower() else (1 if a.isupper() else 2)
    a2 = dm[a] if at==2 else -1

    return (at, a2, a)


s = input()
sorted_str = sorted(s, key=myfunc)

print("".join(sorted_str))

# Create center, left just and right just strings

print(s.center(width, "-"))
print(s.ljust(width, "-"))
print(s.rjust(width, "-"))

# Two features: sort by lambda and using decorators

import operator

def person_lister(f):
    def inner(people:list[list[str]])->list[str]:
        # complete the function
        # sort by age in [first, last, age, sex]
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        outls = [f(p) for p in sorted_people]
        return outls

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    
