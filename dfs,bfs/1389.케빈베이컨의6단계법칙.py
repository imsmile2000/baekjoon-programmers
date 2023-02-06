from collections import deque
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        for i in range(n+1):
            if graph[v][i]==1 and not visited[i]:
                queue.append(i)
                visited[i]=True
                result[i]=result[v]+1

n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
answer=[]
for i in range(1,n+1):
    visited=[False]*(n+1)
    result=[0]*(n+1)
    bfs(graph,i,visited)
    answer.append(sum(result))
print(answer.index(min(answer))+1)