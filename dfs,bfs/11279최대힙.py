import sys
import heapq
n=int(sys.stdin.readline())
maxheap=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if len(maxheap)==0:
            print("0")
        else:
            num=heapq.heappop(maxheap)
            print(-num)
    else:
        heapq.heappush(maxheap,-x)

