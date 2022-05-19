import sys
n=int(sys.stdin.readline())
list1=[0]*10001
for i in range(n):
    x=int(sys.stdin.readline())
    list1[x]+=1
for i in range(10001): #메모리제한이 있을 때는 계수정렬을 사용해야함
    if list1[i]!=0:
        for j in range(list1[i]):
            print(i)