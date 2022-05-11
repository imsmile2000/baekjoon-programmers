import sys
n=int(input())
queue=[]
for i in range(n):
    w=sys.stdin.readline().split() #중요!(메모리 감소)
    if w[0]=='push':
        queue.append(w[1])
    if w[0]=='pop':
        if queue:
            print(queue.pop(0))
        else:
            print("-1")
    if w[0]=='size':
        print(len(queue))
    if w[0]=='empty':
        if len(queue)==0:
            print("1")
        else:
            print("0")
    if w[0]=='front':
        if queue:
            print(queue[0])
        else:
            print("-1")
    if w[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print("-1")
