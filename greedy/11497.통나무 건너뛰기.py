t=int(input())
for i in range(t):
  n=int(input())
  L=list(map(int,input().split()))
  L.sort() #10 11 11 12 12 13 / 2 4 5 7 9
  result=0
  for j in range(2,n):
    l=L[j]-L[j-2] #1 1 1 1 / 3 3 4
    result=max(l,result)
  print(result)