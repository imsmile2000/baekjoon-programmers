n,m=map(int,input().split())
graph=[]
answer=[]
for i in range(n):
    graph.append(input())
for i in range(n-7):
    for j in range(m-7):
        count=0
        count2=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0:
                    if graph[x][y]!="W":
                        count+=1
                    if graph[x][y]!="B":
                        count2+=1
                else:
                    if graph[x][y]!="B":
                        count+=1
                    if graph[x][y]!="W":
                        count2+=1
        answer.append(min(count,count2))
print(min(answer))

