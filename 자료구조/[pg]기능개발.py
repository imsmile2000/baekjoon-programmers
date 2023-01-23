import math
def solution(progresses, speeds):
    days=[]
    for i in range(len(speeds)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    answer=[]
    cnt=1
    M=days[0]
    for i in range(1,len(days)):
        if days[i]<=M:
            M=max(days[i],M)
            cnt+=1
        else:
            M=days[i]
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    print(answer)
    return answer