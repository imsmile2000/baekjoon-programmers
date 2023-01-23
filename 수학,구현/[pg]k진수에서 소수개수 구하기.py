import math
def isprime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
            
def solution(n, k):
    change=''
    count=0
    while n > 0:
        n, mod = divmod(n, k)
        change+=str(mod)
    change=change[::-1].split('0')
    for i in change:
        if i:
            if int(i)!=1 and isprime(int(i))==True:
                count+=1
    return count