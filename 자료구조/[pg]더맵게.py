import heapq
def solution(scoville, K):
    count=0
    heapq.heapify(scoville)
    while scoville[0]<K:
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+(b*2))
        count+=1
        if len(scoville)==1 and scoville[0]<K:
            return -1
            break
    return count