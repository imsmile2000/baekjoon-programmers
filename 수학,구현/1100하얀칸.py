count=0
chess=[[0]*8 for _ in range(8)]
for i in range(8):
    chess[i]=list(map(str,input()))
for i in  range(8):
    for j in range(8):
        if i%2==0 and j%2==0:
            if chess[i][j]=='F':
                count+=1
        if i%2!=0 and j%2!=0:
            if chess[i][j]=='F':
                count+=1

print(count)