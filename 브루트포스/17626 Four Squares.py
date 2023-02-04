import sys
import math
n=int(sys.stdin.readline())
root=int(math.sqrt(n))
def four_squares(n):
    if math.sqrt(n)==root: #n이 제곱수일 경우
        return 1
    for i in range(1,root+1): #n-i^2이 제곱수일 경우
        if int(math.sqrt(n-i**2))==math.sqrt(n-i**2):
            return 2
    for i in range(1,root+1):
        for j in range(1,int(math.sqrt(n-i**2))+1):
            if int(math.sqrt(n-i**2-j**2))==math.sqrt(n-i**2-j**2):
                return 3
    return 4
print(four_squares(n))