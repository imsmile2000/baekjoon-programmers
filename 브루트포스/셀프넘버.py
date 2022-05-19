def dn(n):
    sum=n
    while n>0:
        sum+=(n%10)
        n=(n/10)
    return sum
array=[]
result=0
for i in range(10001):
        result=dn(i)
        if result<10000:
            array[result]=1
        if array[i]!=1:
            print(i)