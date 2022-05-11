N,M,K=map(int,input().split())
num=list(map(int,input().split()))
sum=0
num.sort(reverse=True)
max1=num[0] #가장 큰 수
max2=num[1] #두번째로 큰 수
count=K*(M/(K+1))+M%(K+1)
sum=count*max1+(M-count)*max2
print(int(sum))