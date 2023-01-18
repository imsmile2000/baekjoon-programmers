from collections import deque
def solution(cacheSize, cities):
    cache=deque()
    count=0
    if cacheSize==0:
        return len(cities)*5
    else:
        for i in cities:
            i=i.lower()
            if i not in cache:
                count+=5
                if len(cache)>=cacheSize:
                    cache.popleft()
                    cache.append(i)
                else:
                    cache.append(i)
            else:
                count+=1
                cache.remove(i)
                cache.append(i)
        return count