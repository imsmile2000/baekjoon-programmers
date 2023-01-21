from collections import Counter
def multi(s):
    s=s.lower()
    multi=[]
    for i in range(len(s)-1):
        if s[i:i+2].isalpha()==True:
            multi.append(s[i:i+2])
    return multi
        
def solution(str1, str2):
    str1=multi(str1)
    str2=multi(str2)
    if not str1 and not str2:
        return 65536
    else:
        count1=Counter(str1)
        count2=Counter(str2)
        answer=len(list((count1&count2).elements()))/len(list((count1|count2).elements()))
        return int(answer*65536)