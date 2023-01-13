inputchess=list(map(int,input().split()))
chess=[1,1,2,2,2,8]
count=[0]*6
for i in range(len(chess)):
    count[i]=chess[i]-inputchess[i]
for j in count:
    print(j,end=' ')