# 자신의 크기보다 작은 물고기만 먹을 수 있음
# 먹을 수 있는 물고기가 1마리보다 많다면 거리가 가장 가까운 물고기를 먹으러 감
# 이동시간: 1초, 먹을 때마다 상어 크기가 1 증가
# 아기상어가 몇초동안 물고기를 다 먹을지 출력
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(graph,x,y,shark_size):
    distance=[[0]*n for _ in range(n)] #거리 측정
    visited=[[0]*n for _ in range(n)] #방문여부 측정
    queue=deque()
    queue.append((x,y))
    visited[x][y]=1 #방문 처리
    tmp=[] #먹을 수 있는 물고기 저장
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i] #이동한 x좌표
            ny=y+dy[i] #이동한 y좌표
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]<=shark_size and visited[nx][ny]==0: 
                #아기상어의 크기 보다 작거나 같고, 방문하지 않았다면
                visited[nx][ny]=1 #방문 처리
                distance[nx][ny]=distance[x][y]+1 #거리 +1
                queue.append((nx,ny))
                if graph[nx][ny]<shark_size and graph[nx][ny]!=0:
                    #아기상어의 크기와 같지 않고 빈칸이 아니라면
                    tmp.append((nx,ny,distance[nx][ny]))

    return sorted(tmp,key=lambda x:(-x[2],-x[0],-x[1])) #거리순, 위에 있는 물고기(y좌표), 왼쪽에 있는 물고기(x좌표) 

time=0 #물고기를 잡아먹을 수 있는 시간
count=0
n=int(input())
graph=[[0]*n for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))
shark_size=2 #처음 아기 상어의 크기=2
for i in range(n):
    for j in range(n):
        if graph[i][j]==9: #아기상어 시작점
            x,y=i,j
while True:
    shark=bfs(graph,x,y,shark_size)
    if len(shark)==0: #먹을 물고기(tmp)가 없으면 break
        break
    nx,ny,distance=shark.pop()
    time+=distance #거리, 즉 칸 수만큼 시간 더하기
    graph[x][y]=0 # 물고기를 먹으면 그 칸은 빈칸이 된다
    graph[nx][ny]=0 # 물고기를 먹으면 그 칸은 빈칸이 된다
    x,y=nx,ny # 새로운 칸에서 또 bfs
    count+=1
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다 
    if count==shark_size:
        shark_size+=1
        count=0 # 크기가 증가했으므로 count 초기화
print(time)
