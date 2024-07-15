str_ab=input()
s=[]
for i in str_ab:
    if i=='a':
        s.append(0)
    else:
        s.append(1)
k=str_ab.count('a')
total=sum(s[:k])
answer=[]
for i in range(len(s)):
    if i+k>=len(s):
        total=total-s[i]+s[i+k-len(s)]
    else:
        total=total-s[i]+s[i+k]
    answer.append(total)
print(min(answer))