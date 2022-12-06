t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    for j in range(1,w+1):
        for k in range(1,h+1):
            n-=1
            if n==0:
                result=k*100+j
    print(result)
