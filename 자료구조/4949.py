sentence=[]
while True:
    s=input()
    if s=='.':
        break
    sentence.append(s)

for i in sentence:
    count=[]
    k=0
    for j in i:
        if j=='(' or j=='[':
            count.append(j)
        elif j==')':
            if not count or count[-1]=='[':
                k=-1
                break
            elif count[-1]=='(':
                count.pop()
        elif j==']':
            if not count or count[-1]=='(':
                k=-1
                break
            elif count[-1]=='[':
                count.pop()
    if not count and k!=-1:
        print("yes")
    else:
        print("no")