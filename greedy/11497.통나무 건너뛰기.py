t=int(input())
for i in range(t):
  n=int(input())
  L=list(map(int,input().split()))
  L.sort()
  result=0
  for j in range(2,n):
    l=L[j]-L[j-2]
    result=max(l,result)
  print(result)