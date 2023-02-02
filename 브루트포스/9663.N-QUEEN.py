# 1. 상하좌우 대각선에 이미 위치한 퀸(Queen)이 있는가?
# 2-1. 있으면 퀸을 놓을 수 없음
# 2-2. 없으면 퀸을 놓을 수 있음 count+1 퀸이 n개가 되면 break
# 브루투포스, 백트래킹: DFS 보다 효율적
# col[1]=2: 1행 2열에 퀸이 있음
import sys
n=int(sys.stdin.readline())
count=0
col=[0]*n

def isQueen(i): #1번
    for k in range(i): 
        if col[i]==col[k] or abs(col[i]-col[k])==abs(i-k): #상하좌우, 대각선
            return False
    return True

def nQueen(i): #2번
    global count
    if i==n: #다돌았으면
        count+=1
    else:
        for j in range(n): # n번째 행 돌기
            col[i]=j
            if isQueen(i):
                nQueen(i+1)

nQueen(0)
print(count)
    
