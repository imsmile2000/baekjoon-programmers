from collections import deque
import sys
t=int(sys.stdin.readline())
for i in range(t):
  p=sys.stdin.readline().rstrip()
  n=int(sys.stdin.readline())
  x=deque(sys.stdin.readline().rstrip()[1:-1].split(','))
  count=0
  flag=0
  if n==0:
    x=[]
  for j in p:
    if j=='R':
      count+=1
    elif j=='D':
      if x:
        if count%2==0:
          x.popleft()
        else:
          x.pop()
      else:
        print("error")
        flag=-1
        break
  if flag==0:
    if count%2==0:
      print("["+",".join(x)+"]")
    else:
      x.reverse()
      print("["+",".join(x)+"]")