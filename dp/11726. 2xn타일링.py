n=int(input())
dp=[0]*(n+2)
dp[1]=1
dp[2]=2
if n>=3:
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
print(dp[n]%10007)

#피보나치 수열과 식이 같음
# dp[1]=1
# dp[2]=2
# dp[3]=3
# dp[4]=5