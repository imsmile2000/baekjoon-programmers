from collections import deque
queue=deque()
n,k=map(int,input().split())
for i in range(n):
    queue.append(i+1)
print("<",end='')
for i in range(n):
    for j in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    if len(queue)!=1:
        print(queue[0],end=', ')
    else:
        print(queue[0],end='')
    queue.popleft()
print(">",end='')