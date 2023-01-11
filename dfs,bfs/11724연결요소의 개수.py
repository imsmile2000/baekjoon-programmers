from collections import deque
import sys
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in range(n+1):
            if graph[v][i]==1 and not visited[i]:
                queue.append(i)
                visited[i]=True
        
count=0
n,m=map(int,input().split())
visited=[False]*(n+1)
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u][v]=graph[v][u]=1
#----------------------------------------------여기까지는 bfs 코드
for j in range(1,n+1):
    if not visited[j]: #방문하지 않고
        if graph[j]==0: #그래프가 비었다면
            count+=1
            visited[i]=True #방문처리
        else:
            bfs(graph,j,visited) #bfs
            count+=1
print(count)

    