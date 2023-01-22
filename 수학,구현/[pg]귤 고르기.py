from collections import Counter
def solution(k, tangerine):
    count=list(Counter(tangerine).values())
    count.sort(reverse=True)
    cnt=0
    for i in count:
        if i>=k:
            k=0
            cnt+=1
        elif i<k:
            if k-i>=0:
                k-=i
                cnt+=1
        if k==0:
            break
    return cnt
    