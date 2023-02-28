N,m,M,T,R=map(int,input().split())
X=m
count=0
answer=0
while count<N:
    if m+T>M:
        answer=-1
        break
    if X+T<=M:
        X+=T
        count+=1
    else:
        if X-R<=m:
           X=m
        else:
            X-=R
    answer+=1
print(answer)