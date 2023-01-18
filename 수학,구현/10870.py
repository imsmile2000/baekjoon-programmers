n=int(input())
f=[0]*n
f[1]=1
if n>=2:
  for i in range(2,n):
    f[i]=f[i-1]+f[i-2]
print(f[n-1])