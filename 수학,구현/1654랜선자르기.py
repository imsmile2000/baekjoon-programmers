import sys
k,n=map(int,sys.stdin.readline().split())
lan=[]
for i in range(k):
    lan.append(int(input()))
def binary(n,start,end):
    if start>end:
        print(end)
        return
    mid=(start+end)//2
    count=0
    for i in lan:
        max=i//mid
        count+=max
    if count<n:
        return binary(n,start,mid-1)
    else:
        return binary(n,mid+1,end)
binary(n,1,max(lan))