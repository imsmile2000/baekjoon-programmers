from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y):
    cnt=1 # 1부터 시작임 0부터 아님
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0 #이거 안해줘서 첫번째 오류남
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                cnt+=1
    return cnt
n=int(input())
graph=[[0]*n for _ in range(n)]
count=0
result=[]
for i in range(n):
    graph[i]=list(map(int,input()))
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(graph,i,j))
            count+=1
print(count)
result.sort()
for i in result:
    print(i)