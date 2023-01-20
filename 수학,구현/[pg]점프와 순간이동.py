def solution(n):
    energy=0
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n-=1
            energy+=1
    return energy+1