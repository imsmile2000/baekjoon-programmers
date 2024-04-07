from itertools import permutations
n=int(input())
nlist=list(map(int,input().split()))
order=list(permutations(nlist,n))
max_num=0
for o in order:
    a=sum(abs(o[i]-o[i+1]) for i in range(n-1))
    max_num=max(max_num,a)
print(max_num)