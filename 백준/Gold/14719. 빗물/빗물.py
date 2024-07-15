H,W=map(int,input().split())
block=list(map(int,input().split()))
graph=[[0]*W for _ in range(H)]
for i in range(W):
    for j in range(block[i]):
        graph[H-1-j][i]=1

cnt=0
for row in graph:
    answer=[]
    for i, v in enumerate(row):
        if v==1:
            answer.append(i)
    if len(answer)>=2:
        for n in range(answer[0],answer[-1]):
            if n not in answer:
                cnt+=1

print(cnt)