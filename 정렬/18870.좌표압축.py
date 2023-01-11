n=int(input())
xlist=list(map(int,input().split()))
order_list=list(set(xlist))
order_list.sort() #[-10,-9,2,4]

result={}
for i in range(len(order_list)):
    result[order_list[i]]=i #{-10:0, -9:1, 2:2, 4:3}
for j in range(n):
    print(result[xlist[j]],end=' ')
