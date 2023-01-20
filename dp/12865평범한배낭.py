n,k=map(int,input().split())
bag=[]
for i in range(n):
  w,v=map(int,input().split())
  bag.append((w,v))
bag.sort(key=lambda x:x[1])

dp = [0]*(k+1)
for w, v in bag:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)
print(dp)

# weight=[0]*(n+1)
# value=[0]*(n+1)
# for i in range(1,n+1): #1부터 n까지
#   weight[i]=weight[i-1]+bag[i-1][0] #누적 합으로 더하기
#   value[i]=value[i-1]+bag[i-1][1] #누적 합으로 더하기
#   if weight[i]>k: # 무게가 k보다 커지면
#     value[i]=max(bag[i-1][1],value[i-1]) #이전 누적 가치와 현재 가치 중 큰 것을 선택
#     if bag[i-1][1]>value[i-1]: #현재가치가 더 크면
#       weight[i]=bag[i-1][0] #무게를 현재 무게로 바꾸기 
#     else: #이전 누적가치가 더 크면
#       weight[i]=weight[i-1] #무게를 누적 무게로 바꾸기
# print(value[-1])

