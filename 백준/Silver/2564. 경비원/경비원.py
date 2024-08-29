def distance(d,y): # 원점으로부터의 거리 계산
    if d==1: # 북
        return y
    if d==2: # 남
        return (2*w)+h-y
    if d==3: # 서
        return (2*w)+(2*h)-y
    if d==4: # 동
        return w+y

w,h=map(int,input().split()) # 블록 크기
n=int(input())

store=[]
for i in range(n+1): # 상점 위치와 동근이의 위치 입력 받기
    d,y=map(int,input().split())
    store.append(distance(d,y)) # 절대거리 저장

answer=0
for i in range(n): # 동근이와 상점 사이 최단 거리
    a=abs(store[-1]-store[i]) # store[-1]: 동근이의 위치
    b=2*(w+h) # 블록 전체 길이
    answer+=min(a,b-a) # 시계방향, 반시계 방향 중 최단거리
print(answer)