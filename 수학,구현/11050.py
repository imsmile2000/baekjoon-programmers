import math
n,k=map(int,input().split())
if k>=0 and k<=n:
    result=math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    print(result)
else:
    print("0")