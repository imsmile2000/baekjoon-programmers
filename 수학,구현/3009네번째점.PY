xlist=[]
ylist=[]
for i in range(3):
    x,y=map(int,input().split())
    if x not in xlist:
        xlist.append(x)
    else:
        xlist.remove(x)
    if y not in ylist:
        ylist.append(y)
    else:
        ylist.remove(y)
print(*xlist,*ylist)