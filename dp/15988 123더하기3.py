import sys
t=int(sys.stdin.readline())
dp=[0]*1000001
dp[1]=1
dp[2]=2
dp[3]=4
n=[]
for i in range(t):
    n.append(int(sys.stdin.readline()))

for j in range(4,max(n)+1):
    dp[j]=(dp[j-1]+dp[j-2]+dp[j-3])%1000000009
for k in n:
    print(dp[k])


