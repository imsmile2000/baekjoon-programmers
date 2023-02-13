#fraction 모듈: 분수표현 가능
from fractions import Fraction
n=int(input())
nlist=list(map(int,input().split()))
first=nlist[0]
for i in range(1,len(nlist)):
    fraction=Fraction(first,nlist[i])
    print(str(fraction.numerator)+"/"+str(fraction.denominator))