from math import factorial
n=int(input())
facn=factorial(n)
facn=list(map(int,str(facn)))
count=0
for i in range(len(facn)-1,-1,-1):
    if facn[i]!=0:
        break
    count+=1
print(count)