import sys
n,r,c=map(int,sys.stdin.readline().split())
def Z(n,r,c,count):
    if n==1:
        if r==0 and c==0:
            print(count)
        if r==0 and c==1:
            print(count+1)
        if r==1 and c==0:
            print(count+2)
        if r==1 and c==1:
            print(count+3)
    else: #왼쪽 위는 숫자를 늘릴 필요 없음
        if r<(2**n)//2 and c>=(2**n)//2: #오른쪽 위
            count+=((2**n)//2)**2
            c-=((2**n)//2)
        elif r>=(2**n)//2 and c<(2**n)//2: #왼쪽 아래
            count+=((2**n)//2)**2*2
            r-=((2**n)//2)
        elif r>=(2**n)//2 and c>=(2**n)//2: #오른쪽 아래
            count+=((2**n)//2)**2*3
            r-=((2**n)//2)
            c-=((2**n)//2)
        Z(n-1,r,c,count)
Z(n,r,c,0)