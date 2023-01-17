def round(n):
    if n!=1:
            if n%2==0:
                n=n//2
            else:
                n=(n//2)+1
    return n

def solution(n,a,b):
    count=1
    for i in range(n//2):
        if abs(a-b)==1 and round(a)==round(b):
            break
        a=round(a)
        b=round(b)
        print(a,b)
        count+=1
    return count