import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
hear_name=set()
see_name=set()
answer=set()
for i in range(n):
    hear_name.add(sys.stdin.readline().rstrip())
for j in range(m):
    see_name.add(sys.stdin.readline().rstrip())
answer=hear_name&see_name
print(len(answer))
for i in sorted(answer):
    print(i)