from collections import deque
def bfs(start):
    queue=deque([start])
    visited[start]=1
    while queue:
        n=queue.popleft()
        if n==k:
            return visited[n]-1
        for i in (n-1,n+1,n*2):
            if 0<=i<=100000 and not visited[i]:
                visited[i]=visited[n]+1
                queue.append(i)
        print(visited[n])
n,k=map(int,input().split())
visited=[False]*100001
print(bfs(n))