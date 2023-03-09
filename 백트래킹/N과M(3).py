n,m=map(int,input().split())
visited=[False]*(n+1)
answer=[]
def dfs(depth,n,m):
    if len(answer)==m:
        print(*answer)
        return
    for i in range(1,n+1):
        answer.append(i)
        dfs(i,n,m)
        answer.pop()
dfs(1,n,m)