import math
def solution(n, k):
    person=[i for i in range(1,n+1)]
    result=[]
    k-=1
    for i in range(n,0,-1):
        max_num=math.factorial(n)
        split_num=max_num//n
        result.append(person[k//split_num])
        person.pop(k//split_num)
        k%=split_num
        n-=1
    return result
    