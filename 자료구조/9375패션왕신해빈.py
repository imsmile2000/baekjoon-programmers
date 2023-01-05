import sys
from collections import defaultdict
t=int(sys.stdin.readline())
for i in range(t):
    cloth_set=defaultdict(list)
    sum=1
    n=int(sys.stdin.readline())
    for j in range(n):
        cloth_name,cloth_kind=sys.stdin.readline().split()
        cloth_set[cloth_kind].append(cloth_name)
    for key in cloth_set:
        sum*=(len(cloth_set[key])+1) #각 옷 종류마다 (옷이름의 개수+1) 곱한것
        #조합 공식 기억해두자!
    print(sum-1) #공집합(알몸) 빼기