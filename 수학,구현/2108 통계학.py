from collections import Counter
import sys
n=int(input())
num=[]
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
print(round(sum(num)/n))
print(num[n//2])
count=Counter(num)
most=count.most_common()
if len(most)==1:
    print(most[0][0])
else:
    if most[0][1]==most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
print(num[-1]-num[0])