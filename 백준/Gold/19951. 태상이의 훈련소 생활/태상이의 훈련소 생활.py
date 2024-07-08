N,M=map(int,input().split())
Hlist=list(map(int,input().split()))
jisi=[0]*(N+1)
for i in range(M):
    a,b,k=map(int,input().split())
    jisi[a-1]+=k
    jisi[b]-=k
for i in range(1,N):
    jisi[i]=jisi[i]+jisi[i-1]

for i in range(N):
    Hlist[i]=Hlist[i]+jisi[i]
print(*Hlist)