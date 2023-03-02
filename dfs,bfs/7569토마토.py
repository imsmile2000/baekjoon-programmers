from collections import deque
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
def dfs(graph):
    queue=deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==1:
                    queue.append((i,j,k))
    while queue:
        x,y,z=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=h or ny>=n or nz>=m:
                continue
            if graph[nx][ny][nz]==0:
                graph[nx][ny][nz]=graph[x][y][z]+1
                queue.append((nx,ny,nz))

m,n,h=map(int,input().split())
graph=[[[0]*m for _ in range(n)] for _ in range(h)]
count=0
for i in range(h):
    for j in range(n):
        graph[i][j]=list(map(int,input().split()))
        count+=graph[i][j].count(0)
if count==0:
    print(0)
else:
    dfs(graph)
    count2=0
    M=0
    for i in range(h):
        for j in range(n):
            count2+=graph[i][j].count(0)
            M=max(M,max(graph[i][j]))
    if count2!=0:
        print(-1)
    else:
        print(M-1)

