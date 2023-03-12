n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
answer=[]
def dfs(depth,n,m):
    if len(answer)==m:
        print(*answer)
        return
    for i in range(n):
        if nlist[i] not in answer:#중복방지
            answer.append(nlist[i])
            dfs(depth+1,n,m)
            answer.pop()
dfs(0,n,m)