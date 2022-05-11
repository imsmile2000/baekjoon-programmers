T=int(input())
list1=[]
for _ in range(T):
    N,M=map(int,input().split())
    P=list(map(int,input().split()))
    index=[0 for _ in range(N)]
    index[M]=1
    result=0
    while True:
        if P[0]==max(P):
            result+=1
            if index[0]!=1:
                del P[0]
                del index[0]
            else:
                list1.append(result)
                break
        else:
            P.append(P[0])
            index.append(index[0])
            del P[0]
            del index[0]
for i in list1:
    print(i)

