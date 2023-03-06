n,m=map(int,input().split())
answer=[]
def dfs(depth,n,m):
    if depth==m:
        print(*answer)
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=True
            answer.append(i)
            dfs(depth+1,n,m)
            visited[i]=False
            answer.pop()
visited=[False]*(n+1)
dfs(0,n,m)