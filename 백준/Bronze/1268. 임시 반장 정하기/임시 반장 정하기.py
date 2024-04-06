n=int(input())
student=[]
answer=[]
for i in range(n):
    student.append(list(map(int,input().split())))

for i in range(n):
    count=[]
    for j in range(5):
        for a,b in enumerate([row[j] for row in student]):
            if b==student[i][j]:
                count.append(a+1)
    answer.append(len(set(count)))
print(answer.index(max(answer))+1)