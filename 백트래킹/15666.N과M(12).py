n,m=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
answer=[]
def dfs(depth,n,m):
    if len(answer)==m:
        print(*answer)
        return
    x=0
    for i in range(depth,n):
        if x!=nlist[i]: # x가 list의 숫자와 같지 않다면(중복되는 수열 여러번 출력x)
            answer.append(nlist[i])
            dfs(i,n,m) #비내림차순
            x=nlist[i]
            answer.pop()
dfs(0,n,m)