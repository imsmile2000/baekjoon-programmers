n=int(input())
sum1=0
count=0
start=0
end=0
while end<=n:
    if sum1<n: # 총합이 n보다 작으면
        end+=1
        sum1+=end
    elif sum1>n:
        sum1-=start
        start+=1
    else:
        count+=1
        end+=1
        sum1+=end
print(count)

