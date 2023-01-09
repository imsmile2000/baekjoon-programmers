n=int(input())
graph=[[0]*n for _ in range(n)]
for i in range(n):
    graph[i]=list(map(int,input().split()))
minus_one=0
zero=0
one=0
def  paper_num(n,div_graph):
    global minus_one
    global zero
    global one
    count=0
    zero_count=0
    for i in range(n):
        count+=sum(div_graph[i])
        zero_count+=div_graph[i].count(0)
    if count==n**2:
        one+=1
    elif count==-(n**2):
        minus_one+=1
    elif zero_count==n**2:
        zero+=1
    else:
        divide=[div_graph[i][:n//3] for i in range(n//3)] #사각형 9개로 나눴을 때 왼쪽 위
        paper_num(n//3,divide)
        divide=[div_graph[i][n//3:(2*n)//3] for i in range(n//3)]
        paper_num(n//3,divide)
        divide=[div_graph[i][(2*n)//3:] for i in range(n//3)]
        paper_num(n//3,divide)
        divide=[div_graph[i][:n//3] for i in range(n//3,(2*n)//3)]
        paper_num(n//3,divide)
        divide=[div_graph[i][n//3:(2*n)//3] for i in range(n//3,(2*n)//3)]
        paper_num(n//3,divide)
        divide=[div_graph[i][(2*n)//3:] for i in range(n//3,(2*n)//3)]
        paper_num(n//3,divide)
        divide=[div_graph[i][:n//3] for i in range((2*n)//3,n)]
        paper_num(n//3,divide)
        divide=[div_graph[i][n//3:(2*n)//3] for i in range((2*n)//3,n)]
        paper_num(n//3,divide)
        divide=[div_graph[i][(2*n)//3:] for i in range((2*n)//3,n)]
        paper_num(n//3,divide)

paper_num(n,graph)
print(minus_one)
print(zero)
print(one)