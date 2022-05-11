N,M=map(int,input().split())
list1=[]
for i in range(N):
    num=list(map(int,input().split()))
    num.sort()
    list1.append(num[0])
print(max(list1))