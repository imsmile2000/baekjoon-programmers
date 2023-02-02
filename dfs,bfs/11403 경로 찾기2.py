n=int(input())
graph=[[0]*n for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k)
            if graph[j][i]==1 and graph[i][k]==1:
                graph[j][k]=1

for i in range(n):
    print(*graph[i])