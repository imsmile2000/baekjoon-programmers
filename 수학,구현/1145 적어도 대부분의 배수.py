nlist=list(map(int,input().split()))
n=min(nlist)
while True:
    count=0
    for i in nlist:
        if n%i==0:
            count+=1
    if count>2:
        print(n)
        break
    n+=1