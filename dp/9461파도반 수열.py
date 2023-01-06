t=int(input())
for i in range(t):
    n=int(input())
    dp=[0]*(n+3)
    dp[0]=dp[1]=dp[2]=1
    if n>=3:
        for j in range(3,n):
            dp[j]=dp[j-2]+dp[j-3]
    print(dp[n-1])