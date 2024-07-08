N=int(input())
tower=list(map(int,input().split()))
answer=[0]*N
stack=[]
for i in range(N):
    while stack:
        # print(stack,tower[i])
        if stack[-1][1]>=tower[i]:
            answer[i]=stack[-1][0]+1 # 수신 탑 idx
            break
        else:
            stack.pop()
    stack.append((i,tower[i])) # (0,6) (1,9) (2,5) (3,7) (4,4)
print(*answer)