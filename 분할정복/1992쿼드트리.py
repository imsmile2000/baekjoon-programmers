n=int(input())
graph=[[0]*n for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input()))
result=[]
def quad_tree(n,div_graph):
    global result
    one_num=0
    for i in range(n):
        one_num+=sum(div_graph[i])
    if one_num==0:
        result.append(0)
    elif one_num==n**2:
        result.append(1)
    else:
        result.append('(')
        divide=[div_graph[i][:n//2] for i in range(n//2)] #사각형 네개로 나눴을 때 왼쪽 위
        quad_tree(n//2,divide)
        divide=[div_graph[i][n//2:] for i in range(n//2)] #오른쪽 위
        quad_tree(n//2,divide)
        divide=[div_graph[i][:n//2] for i in range(n//2,n)] # 왼쪽 아래
        quad_tree(n//2,divide)
        divide=[div_graph[i][n//2:] for i in range(n//2,n)] # 오른쪽 아래
        quad_tree(n//2,divide)
        result.append(')')
quad_tree(n,graph)
for i in result:
    print(i,end='')