import heapq
import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    minqueue=[]
    maxqueue=[]
    visited=[0]*n
    for j in range(n):
        pqueue=sys.stdin.readline().rstrip()
        if pqueue.split()[0]=='I':
            x=int(pqueue.split()[1])
            heapq.heappush(minqueue,(x,j))
            heapq.heappush(maxqueue,(-x,j))
            visited[j]=1
        elif pqueue=='D -1': #최소값 삭제
            while minqueue and not visited[minqueue[0][1]]: #maxqueue에서 사라진 값 삭제
                heapq.heappop(minqueue)
            if minqueue:
                visited[minqueue[0][1]]=0
                heapq.heappop(minqueue)
        elif pqueue=='D 1': #최대값 삭제
            while maxqueue and not visited[maxqueue[0][1]]: #minqueue에서 사라진값 삭제
                heapq.heappop(maxqueue)
            if maxqueue:
                visited[maxqueue[0][1]]=0
                heapq.heappop(maxqueue)

    while minqueue and not visited[minqueue[0][1]]:
        heapq.heappop(minqueue)
    while maxqueue and not visited[maxqueue[0][1]]:
        heapq.heappop(maxqueue)

    if not maxqueue or not minqueue:
        print("EMPTY")
    else:
        print(-maxqueue[0][0],minqueue[0][0])