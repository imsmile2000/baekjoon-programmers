n,m=map(int,input().split())
visited=[False]*(n+1)
answer=[]
def dfs(depth,n,m):
    if len(answer)==m:
        print(*answer)
        return
    for i in range(depth,n+1):
        if i not in answer:
            answer.append(i)
            dfs(i+1,n,m)
            answer.pop()
dfs(1,n,m)
