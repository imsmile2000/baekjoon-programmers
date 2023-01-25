import math
t=int(input())
for i in range(t):
  x1,y1,r1,x2,y2,r2=map(int,input().split())
  distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
  if x1==x2 and y1==y2 and r1==r2:
    print(-1)
  elif r1+r2==distance or abs(r1-r2)==distance:
    print(1)
  elif r1+r2>distance and abs(r1-r2)<distance:
    print(2)
  elif r1+r2<distance or abs(r1-r2)>distance:
    print(0)