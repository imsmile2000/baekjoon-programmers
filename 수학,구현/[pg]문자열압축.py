def solution(s):
    answer=[]
    if len(s)==1:
        return 1
    else:
        for i in range(1,(len(s)//2)+1):
            queue=[]
            string=s
            result=''
            while string:
                slice=string[:i]
                string=string[i:]
                if queue:
                    if slice==queue[-1][1]:
                        queue[-1][0]+=1
                    else:
                        queue.append([1,slice])
                else:
                    queue.append([1,slice])
            for j in queue:
                if j[0]>1:
                    result=result+str(j[0])
                result=result+str(j[1])
            answer.append(len(result))
        return min(answer)