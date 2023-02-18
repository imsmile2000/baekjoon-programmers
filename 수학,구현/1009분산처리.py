import sys
t=int(sys.stdin.readline())
for i in range(t):
    a,b=map(int,sys.stdin.readline().split())
    answer=(a**b)%10
    if answer==0:
        print(10)
    else:
        print(answer)