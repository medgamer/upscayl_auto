
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
