from collections import deque
def bfs(graph,start,visited): #bfs
    queue=deque([start])
    queue.append(start)
    while queue:
        v=queue.popleft()
        for i in range(n):
            if graph[v][i]==1 and not visited[i]:
                queue.append(i)
                visited[i]=True
                result[start][i]=1 #result[0][i]=1, result[1][i]=1...

n=int(input())
graph=[[0]*n for _ in range(n)]
result=[[0]*n for _ in range(n)] #정답 인접행렬
for i in range(n):
    graph[i]=list(map(int,input().split()))

for i in range(n):
    visited=[False]*n #매번 visited를 초기화해야함
    bfs(graph,i,visited) #bfs(0)~bfs(n-1)까지

for i in result: #인접행렬 출력
    print(*i)