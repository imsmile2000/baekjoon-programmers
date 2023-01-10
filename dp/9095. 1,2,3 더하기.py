import sys
t=int(sys.stdin.readline())
dp=[0,1,2,4,0,0,0,0,0,0,0,0]
for i in range(t):
    n=int(sys.stdin.readline())
    for j in range(4,n+1):
        dp[j]=dp[j-1]+dp[j-2]+dp[j-3]
    print(dp[n])
