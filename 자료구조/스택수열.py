from collections import deque
n=int(input())
deq=deque(i+1 for i in range(n))
count=0
while len(deq)>1:
    deq.popleft() #맨 왼쪽 pop
    deq.append(deq.popleft())
    count+=1
print(deq[0])