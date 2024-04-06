a,b=map(int,input().split())
total=0
for i in range(46):
    for j in range(a,b+1):
        if i*(i-1)/2< j and j<=i*(i+1)/2:
            total+=i
print(total)