import sys
n=int(sys.stdin.readline())
kg=[]
cm=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    kg.append(x)
    cm.append(y)
rank=[1]*n
for i in range(n):
    for j in range(i+1,n):
        if kg[i]>kg[j] and cm[i]>cm[j]:
            rank[j]+=1
        elif kg[i]<kg[j] and cm[i]<cm[j]:
            rank[i]+=1
for i in rank:
    print(i,end=' ')
    
