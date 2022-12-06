N,K=map(int,input().split(" "))
circle=[]
for i in range(N):
    circle.append(i+1)
k=0
while True:
    k+=K
    if k<=len(circle):
        circle.pop(k-1)
    elif k>len(circle):
        k-=len(circle)
        circle.pop(k-1)
    if not circle:
        break

