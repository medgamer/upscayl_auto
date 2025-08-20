
import numpy as np

np.set_printoptions(legacy='1.13')

# Get one line input of numbers as string and split into list
s = input()
int_list = [int(num) for num in s.split()]

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
