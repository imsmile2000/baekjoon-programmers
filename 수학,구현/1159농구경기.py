import sys
n=int(sys.stdin.readline().rstrip())
name_dict={}
for i in range(n):
    name=sys.stdin.readline()
    if name[0] in name_dict:
        name_dict[name[0]]+=1
    else:
        name_dict[name[0]]=1
answer=[]
for i,j in name_dict.items():
    if j>=5:
        answer.append(i)
answer.sort()
if len(answer)!=0:
    print(''.join(map(str,answer)))
else:
    print("PREDAJA")

