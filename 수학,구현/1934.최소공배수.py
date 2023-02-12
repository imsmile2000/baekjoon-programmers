import math
t=int(input())
def lcd(a,b):
    return (a*b)//math.gcd(a,b)
for i in range(t):
    a,b=map(int,input().split())
    print(lcd(a,b))