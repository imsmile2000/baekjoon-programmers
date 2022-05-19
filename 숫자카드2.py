from sys import stdin
from collections import Counter
n=stdin.readline().rstrip()
nlist=list(map(int,stdin.readline().split()))
m=stdin.readline().rstrip()
mlist=list(map(int,stdin.readline().split()))
count=Counter(nlist)
for i in range(int(m)):
    if mlist[i] in count:
        print(count[mlist[i]],end=' ')
    else:
        print(0,end=' ')