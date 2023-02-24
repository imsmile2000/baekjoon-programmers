import sys
from collections import deque
n=int(sys.stdin.readline())
queue=deque()
queue.append([n])
result=[]
while queue:
    q=queue.popleft()
    i=q[0]
    if i==1:
        result=q
        break
    if i%3==0:
        queue.append([i//3]+q)
    if i%2==0:
        queue.append([i//2]+q)

    queue.append([i-1]+q)

print(len(result)-1)
result.reverse()
print(*result)


