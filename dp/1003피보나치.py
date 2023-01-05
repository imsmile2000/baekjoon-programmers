import sys
import time
t=int(sys.stdin.readline())    
for i in range(t):
    num=int(sys.stdin.readline())
    zero=[1,0,1]
    one=[0,1,1]
    if num>=3:
        for j in range(2,num):
            zero.append(zero[j-1]+zero[j])
            one.append(one[j-1]+one[j])
    print(zero[num],one[num])

