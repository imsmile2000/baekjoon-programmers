t=int(input())
for i in range(t):
    ps=input()
    count=0
    for j in ps:
        if j=='(':
            count+=1
        elif j==')':
            count-=1
        if count<0:
            break
    if count==0:
        print("YES")
    else:
        print("NO")