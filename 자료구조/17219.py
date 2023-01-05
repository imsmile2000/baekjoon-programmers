import sys
n,m=map(int,sys.stdin.readline().split())
password={}
for i in range(n):
    s,p=sys.stdin.readline().split()
    password[s]=p
for j in range(m):
    site=sys.stdin.readline().rstrip()
    print(password[site])