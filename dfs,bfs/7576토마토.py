from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(graph):
    queue=deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))


m,n=map(int,input().split())
graph=[[0]*m for _ in range(n)]
count=0
count2=0
M=0
for i in range(n):
    graph[i]=list(map(int,input().split()))
    count+=graph[i].count(0)
if count==0:
    print(0)
else:
    dfs(graph)
    for j in range(n):
        count2+=graph[j].count(0)
        M=max(M,max(graph[j]))
    if count2!=0:
        print(-1)
    else:
        print(M-1)