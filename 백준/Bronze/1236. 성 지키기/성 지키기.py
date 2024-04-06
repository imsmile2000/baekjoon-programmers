n,m=map(int,input().split())
castle=[]
for i in range(n):
    castle.append(list(map(str,input())))

#가로에 X 없으면 +1
cnt1=0
for i in range(n):
    if castle[i].count('X')==0:
        cnt1+=1
#세로줄에 X 없으면 +1
cnt2=0
for j in range(m):
    if 'X' not in [row[j] for row in castle]:
            cnt2+=1

print(max(cnt1,cnt2))