import sys
n,m=map(int,sys.stdin.readline().split())
pocketmon={}
pocketmon2={}
for i in range(1,n+1):
    eng=sys.stdin.readline().rstrip()
    pocketmon[i]=eng
    pocketmon2[eng]=i
for j in range(m):
    find=sys.stdin.readline().rstrip()
    if find.isdigit():
        print(pocketmon[int(find)])
    else:
        print(pocketmon2[find])
