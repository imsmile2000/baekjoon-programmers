def solution(brown, yellow):
    total=brown+yellow
    for x in range(1,total//2):
        if (x-2)*((total/x)-2)==yellow:
            return [total/x,x]