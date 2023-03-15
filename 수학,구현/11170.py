t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    count=0
    for j in range(n,m+1):
        if '0' in str(j):
            count+=str(j).count('0')
    print(count)