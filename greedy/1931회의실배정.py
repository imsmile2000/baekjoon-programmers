n=int(input())
meeting=[]
for i in range(n):
    start,end=map(int,input().split())
    meeting.append((start,end))
meeting.sort(key=lambda x:(x[1],x[0]))
connect=0
count=0
for a,b in meeting:
    if a>=connect:
        connect=b
        count+=1
print(count)
    