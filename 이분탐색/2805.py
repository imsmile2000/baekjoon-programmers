import sys
n,m=map(int,sys.stdin.readline().split())
h=list(map(int,sys.stdin.readline().split()))
start=1
end=max(h)
while start<=end:
    mid=(start+end)//2
    newh=0
    for i in h:
        if i>mid:
            newh+=(i-mid)
            if newh>m:
                break
    if newh>=m:
        start=mid+1
    elif newh<m:
        end=mid-1
print(end)