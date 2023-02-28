import sys
for i in range(3):
    n=int(sys.stdin.readline())
    sum=0
    for j in range(n):
        num=int(sys.stdin.readline())
        sum+=num
    if sum==0:
        print(0)
    elif sum>=0:
        print("+")
    else:
        print("-")
