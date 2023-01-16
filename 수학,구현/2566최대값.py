graph=[[0]*9 for _ in range(9)]
maxnum=[]
for i in range(9):
    graph[i]=list(map(int,input().split()))
    maxnum.append(max(graph[i]))
print(max(maxnum))
row=maxnum.index(max(maxnum))
print(row+1,graph[row].index(max(graph[row]))+1)