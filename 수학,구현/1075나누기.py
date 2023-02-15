n=int(input())
f=int(input())
num=(n//100)*100
for i in range(num,num+100):
    if i%f==0:
        i=list(map(int,str(i)))
        print(''.join(map(str,i[-2:])))
        break