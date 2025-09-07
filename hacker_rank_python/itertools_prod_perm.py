
from itertools import permutations, product, combinations, combinations_with_replacement, groupby

a = [1,2,3]
b = [4,5,6]

c = list(product(a,b))

s = "ABCD"
# all perm of length 2 substr.
d = permutations(s,2)

# max sum of 7 elements selected from 7 lists using product().
s = input()
k,m = [int(num) for num in s.split()]

pls = []
for i in range(k):
    s = input().split()
    ni = int(s[0])
    sn = [int(s[i])*int(s[i])%m for i in range(1, ni+1)]
    if i==0:
        pls = sn
    else:
        pl = list(product(pls, sn))
        pls = [(i+j)%m for (i,j) in pl]

print(max(pls))

# Counter solution

from collections import Counter

ns = int(input())
s = input()
shoes = [int(num) for num in s.split()]

nc = int(input())

counter = Counter()
for i in range(nc):
    si, pr = [int(num) for num in input().split()]
    if si in shoes:
        counter += Counter({si : pr})
        shoes.remove(si)

print(counter.total())

# OrderedDict solved by Counter

from collections import Counter

n = int(input())

counter = Counter()

for i in range(n):
    s = input().split()
    if len(s)==2:
        counter += Counter({s[0] : int(s[1])})
    else:
        counter += Counter({s[0]+" "+s[1] : int(s[2])})

for it in counter:
    print(it, counter[it])


# set operations
ne = int(input())
s = input()
es = set([int(num) for num in s.split()])

nf = int(input())
s = input()
fs = set([int(num) for num in s.split()])

print(len(es.difference(fs)))

from collections import defaultdict

s = input()
n,m = [int(num) for num in s.split()]

a = defaultdict()
for i in range(1, n+1):
    v = input()
    if v in a:
        a[v].append(i)
    else:
        a[v] = [i]

for i in range(m):
    v = input()
    if v in a:
        print(*a[v])
    else:
        print(-1)

import calendar

s = input()
m,d,y = [int(num) for num in s.split()]

wd =calendar.weekday(y, m, d)

print(calendar.day_name[wd].upper())
