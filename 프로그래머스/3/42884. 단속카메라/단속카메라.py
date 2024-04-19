def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[0],x[1]))
    cam=routes[0]
    for i in routes[1:]:
        if i[0]<=cam[1]: # 시작 점이랑 끝점이 겹치면
            cam=[i[0],min(i[1],cam[1])]
        else:
            cam = i
            answer+=1
    return answer+1

