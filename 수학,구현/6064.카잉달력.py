t=int(input())
# x%n==y%n을 만족하는 x,y가 있는지 확인해야함
for i in range(t):
    m,n,x,y=map(int,input().split())
    count=0
    while x<=(m*n):
        if x%n==y%n:# y%n=9%12=9
            # x%n = 3%12-> 13%12-> 23%12-> 33%12=9 x=33
            print(x)
            break
        x+=m
    if x>m*n:
        print(-1)

