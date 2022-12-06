n=int(input())
num=[i for i in range(n,0,-1)]
stack=[]
count=1
result=[]
for i in range(n):
    s=int(input())
    while count<=s:
        stack.append(count)
        count+=1
        result.append("+")
    if s==stack[-1]:
        stack.pop()
        result.append("-")
    else:
        result.append("N")
if "N" in result:
    print("NO")
else:
    for i in result:
        print(i)    
