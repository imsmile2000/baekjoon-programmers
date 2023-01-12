def solution(operations):
    queue=[]
    for i in operations:
        if i.split()[0]=='I':
            queue.append(int(i.split()[1]))
        elif i=='D 1':
            if queue:
                queue.sort()
                queue.pop()
        elif i=='D -1':
            if queue:
                queue.sort(key=lambda x:-x)
                queue.pop()
                            
    if queue:
        queue.sort(key=lambda x:-x)
        return [queue[0],queue[-1]]
    else:
        return [0,0]