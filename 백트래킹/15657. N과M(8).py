n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
answer=[]
def dfs(depth,n,m):
    if len(answer)==m:
        print(*answer)
        return
    for i in range(depth,n):
        answer.append(nlist[i])
        dfs(i,n,m)
        answer.pop()
dfs(0,n,m)