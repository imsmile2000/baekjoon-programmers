n=int(input())
if n==1:
    print("1")
elif n>1 and n<=7:
    print("2")
else:
    for i in range(2,n//2):
        if n<=(3*i*i)-(3*i)+1 and n>(3*i*i)-(9*n)+7:
            print(i)
            break