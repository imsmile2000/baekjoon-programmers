import sys
n,m,b=map(int,sys.stdin.readline().split()) #b:인벤토리에 있는 개수
craft=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans=sys.maxsize
height=0

for g in range(257): #땅의 높이는 256 이하
    plus=0  # 놓는 블록의 수
    minus=0 # 인벤토리에 넣는 블록의 수
    for i in range(n): 
        for j in range(m):
            if craft[i][j]>=g:
                minus+=craft[i][j]-g
            else:
                plus+=g-craft[i][j]
    if plus<=minus+b: #꺼내는 블록의 수가 (인벤토리+인벤토리에 넣는 블록의 수)보다 작을 때
        time=plus+(minus*2)
        if time<=ans: 
            ans=time
            height=g
print(ans,height)

