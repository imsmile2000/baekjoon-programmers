import sys
n=int(sys.stdin.readline())
dp_in=[0]*(n+1)
for i in range(n):
    k=int(sys.stdin.readline().rstrip())
    dp_in[i]=k
# dp_in =10 20 15 25 10 20
dp=[0]*(n+1)
dp[0]=dp_in[0]
dp[1]=dp_in[0]+dp_in[1]
if n>=2: #n=1이면 indexerror 뜸 if문 설정 안해줘서 error 뜸
    dp[2]=max(dp_in[0]+dp_in[2],dp_in[1]+dp_in[2])
# 초기화 dp=10, 30, 35, 0, 0, 0 
for j in range(3,n):
    dp[j]=max(dp_in[j]+dp_in[j-1]+dp[j-3],dp_in[j]+dp[j-2])
print(dp[n-1])
# [10, 30, 35, 55, 0, 0]
# [10, 30, 35, 55, 65, 0]
# [10, 30, 35, 55, 65, 75]
# [10, 30, 35, 55, 65, 75]
