import sys
n,m=map(int,sys.stdin.readline().split())
nlist=list(map(int,sys.stdin.readline().split()))
result=[0]
sum=0
for i in nlist:
    sum+=i
    result.append(sum)
for i in range(m):
    i,j=map(int,sys.stdin.readline().split())
    print(result[j]-result[i-1])