import sys
n,k=map(int,sys.stdin.readline().split())
coin=set()
for i in range(n):
    coin.add(int(sys.stdin.readline().rstrip()))
count=0
for i in sorted(coin,reverse=True):
    if k==0:
        break
    if i<=k:
        count+=(k//i)
        k-=(i*(k//i))
print(count)
