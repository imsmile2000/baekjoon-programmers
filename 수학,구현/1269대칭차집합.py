from collections import Counter
anum,bnum=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count1=Counter(a)
count2=Counter(b)
print(len(list((count1-count2).elements()))+len(list((count2-count1).elements())))