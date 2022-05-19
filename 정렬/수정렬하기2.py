import sys
n=int(sys.stdin.readline())
list1=[]
for i in range(n):
    x=int(sys.stdin.readline())
    list1.append(x)
list1.sort()
for i in list1:
    print(i)