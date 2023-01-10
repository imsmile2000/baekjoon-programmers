def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')
    for i in range(n+1):
        if graph[v][i]==0 and not visited[i]:
            dfs(graph,i,visited)

n,m=map(int,input().split())
visited=[False]*(n+1)
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u][v]=graph[v][u]=1
dfs(graph,1,visited)
print(graph)