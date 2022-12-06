from collections import deque
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(str,input())))
visited=[[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()

def init():
    x1,y1,x2,y2=[0]
    for i in range(N):
        for j in range(M):
            if graph[i][j]=='R':
                x1,y1=i,j
            if graph[i][j]=='B':
                x2,y2=i,j
    queue.append((x1,y1,x2,y2,1))
    visited[x1][y1][x2][y2] = True

def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수 
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    init()
    while queue:
        x1,y1,x2,y2,depth=queue.popleft()
        if depth>10:
            break
        for i in range(4):
            rx,ry,rcount=move(x1,y1,dx[i],dy[i])
            bx,by,bcount=move(x2,y2,dx[i],dy[i])
            if graph[bx][by]=='O':
                continue
            if graph[rx][ry]=='O':
                print(depth)
                return
            if rx==bx and ry==by:
                if rcount>bcount:
                    rx-=dx[i]
                    ry-=dy[i]
                else:
                    bx-=dx[i]
                    by-=dy[i]
            if not visited[rx][ry][bx][by]:
                visited[rx][ry][bx][by]=True
                queue.append((rx,ry,bx,by,depth+1))
    print(-1)
bfs()
