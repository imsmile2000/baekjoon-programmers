import sys
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    people=[i for i in range(1,n+1)]
    for a in range(k):
        for b in range(1,n):
            people[b]+=people[b-1]
    print(people[-1])
    