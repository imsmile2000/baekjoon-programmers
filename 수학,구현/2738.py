n,m=map(int,input().split())
matrixa=[list(map(int,input().split())) for _ in range(n)]
matrixb=[list(map(int,input().split())) for _ in range(n)]
answer=[[0]*m for _ in range(n)]

for x in range(n):
    for y in range(m):
        answer[x][y]=matrixa[x][y]+matrixb[x][y]

for i in range(len(answer)):
    print(*answer[i])
