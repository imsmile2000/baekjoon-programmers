n=int(input())
nlist=list(map(int,input().split()))
nlist.sort()
start=0
end=n-1
sum=[]
idx=[]
while start<end:
    s=nlist[start]+nlist[end]
    if s<0: #두용액의 합이 0보다 작으면
        idx.append(abs(s))
        sum.append((nlist[start],nlist[end])) 
        start+= 1 # 1, 2, ....
    elif s>0: #두용액의 합이 0보다 작으면
        idx.append(abs(s))
        sum.append((nlist[start],nlist[end]))
        end-= 1 # n-2, n-3, ....
    else:
        idx.append(abs(s))
        sum.append((nlist[start],nlist[end]))
        break
k=idx.index(min(idx))
print(*sum[k])
