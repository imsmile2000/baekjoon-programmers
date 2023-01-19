from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y):
  queue=deque()
  queue.append((x,y))
  graph[x][y]=0
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=0
        queue.append((nx,ny))

t=int(input())
for i in range(t):
  count=0
  m,n,k=map(int,input().split())
  graph=[[0]*m for _ in range(n)]
  for j in range(k):
    x,y=map(int,input().split())
    graph[y][x]=1
  for x in range(m):
    for y in range(n):
      if graph[y][x]==1:
        bfs(graph,y,x)
        count+=1
  print(count)
  