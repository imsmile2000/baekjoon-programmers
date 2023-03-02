import datetime
def solution(n, t, m, timetable):
    shuttle=[540+t*i for i in range(n)]
    time=[]
    for i in timetable:
        time.append(int(i[0:2])*60+int(i[3:]))
    time.sort()
    answer=0
    j=0
    for i in shuttle:
        count=m
        while j<len(time) and time[j]<=i and count>0: # 크루의 도착시간이 셔틀시간보다 빠르고 자리가 남아 있으면
                count-=1
                j+=1
        if count>0:
            answer=i
        else:
            answer=time[j-1]-1
    return format(answer//60,'02')+":"+format(answer%60,'02')
            
                

        
        
        
        
        