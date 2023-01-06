def dfs(graph,v,visited):
    visited[v]=True
    # print(v,end=' ')
    for i in range(n+1):
        if graph[v][i]==1 and not visited[i]:
            dfs(graph,i,visited)

n=int(input())
connected=int(input())            
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(connected):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

dfs(graph,1,visited)
print(visited.count(True)-1)

