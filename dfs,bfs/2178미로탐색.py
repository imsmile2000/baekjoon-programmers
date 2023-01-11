from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y): #좌표
    queue=deque()
    queue.append((x,y)) #input 좌표 -시작점
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i] 
            ny=y+dy[i] #상하좌우 탐색
            if nx<0 or ny<0 or nx>=n or ny>=m: #그래프를 벗어나면
                continue
            if graph[nx][ny]==0: #이동할 수 없는 칸이면
                continue
            if graph[nx][ny]==1: #이동할 수 있는 칸이면
                graph[nx][ny]=graph[x][y]+1 #한칸 count
                queue.append((nx,ny)) 
    return graph[n-1][m-1] #그래프 탈출구까지의 최단거리
        
n,m=map(int,input().split())
graph=[[0]*m for _ in range(n)]
visited=[False]*(n+1)
for i in range(n):
    graph[i]=list(map(int,input()))
print(bfs(0,0)) #0,0부터 미로 시작
