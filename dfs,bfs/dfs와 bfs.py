from collections import deque
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in range(N+1):
        if graph[v][i]==1 and not visited[i]:
            dfs(graph,i,visited)
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in range(N+1):
            if graph[v][i]==1 and not visited[i]:
                queue.append(i)
                visited[i]=True

N,M,V=map(int,input().split())
visited=[False]*(N+1)
visited2=[False]*(N+1)
graph=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

dfs(graph,V,visited)
print()
bfs(graph,V,visited2)