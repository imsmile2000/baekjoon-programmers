n=int(input())
nlist=list(map(int,str(n)))
l=len(nlist)
result=0
if n<18:
    for i in range(1,n):
        sum=i
        ilist=list(map(int,str(i)))
        for j in range(len((ilist))):
            sum+=ilist[j]
        if sum==n:
            result=i
            break
else:
    for i in range(n-(9*l),n-l+1):
        sum=i
        ilist=list(map(int,str(i)))
        for j in range(len((ilist))):
            sum+=ilist[j]
        if sum==n:
            result=i
            break
if result==0:
    print("0")
else:
    print(result)