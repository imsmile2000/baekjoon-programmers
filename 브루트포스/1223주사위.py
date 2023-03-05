from collections import Counter
s1,s2,s3=map(int,input().split())
dice1=[i for i in range(1,s1+1)]
dice2=[i for i in range(1,s2+1)]
dice3=[i for i in range(1,s3+1)]
result=[]
for i in dice1:
    for j in dice2:
        for k in dice3:
            result.append(i+j+k)
c=Counter(result)
answer=0
print(c.most_common(1)[0][0])