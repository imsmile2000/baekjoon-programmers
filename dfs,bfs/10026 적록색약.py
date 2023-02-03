from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y):
    queue=deque()
    queue.append((x,y))
    color=graph[x][y]
    graph[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==color:
                graph[nx][ny]=0
                queue.append((nx,ny))

n=int(input())
graph=[[0]*n for _ in range(n)]
rd_graph=[[0]*n for _ in range(n)]
for i in range(n):
    k=input()
    graph[i]=list(map(str,k))
    rd_graph[i]=list(k.replace('G','R'))
count=0
count2=0
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            bfs(graph,i,j)
            count+=1
for i in range(n):
    for j in range(n):
        if rd_graph[i][j]!=0:
            bfs(rd_graph,i,j)
            count2+=1
print(count,count2)