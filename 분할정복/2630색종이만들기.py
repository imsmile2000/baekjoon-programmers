n=int(input())
graph=[]
white=0
blue=0
for i in range(n):
        graph.append(list(map(int,input().split())))

def divideconquer(n,div_graph):
    global white
    global blue
    one_num=0
    for i in range(n):
        one_num+=sum(div_graph[i])
    if one_num==0: #전부다 0이면
        white+=1
    elif one_num==n**2: #전부다 1이면
        blue+=1
    else:
        divide=[div_graph[i][:n//2] for i in range(n//2)] #사각형 네개로 나눴을 때 왼쪽 위
        divideconquer(n//2,divide)
        divide=[div_graph[i][n//2:] for i in range(n//2)] #오른쪽 위
        divideconquer(n//2,divide)
        divide=[div_graph[i][:n//2] for i in range(n//2,n)] # 왼쪽 아래
        divideconquer(n//2,divide)
        divide=[div_graph[i][n//2:] for i in range(n//2,n)] # 오른쪽 아래
        divideconquer(n//2,divide)
        
divideconquer(n,graph) #맨처음 n*n 그래프
print(white)
print(blue)

