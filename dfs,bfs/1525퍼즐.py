# 2차원 배열을 문자열로 정렬시킨다고 생각
# [[1,2,3],[4,5,6],[7,8,9]] -> '1234567890'
from collections import deque
graph_to_str=""
for i in range(3):
    graph_to_str+="".join(list(input().split())) #2차원 배열 문자열로 바꾸기
visited={graph_to_str:0} #key: 현재 퍼즐 모습, value: 움직인 횟수
queue=deque([graph_to_str])
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs():
    while queue:
        graph_to_str=queue.popleft()
        idx=graph_to_str.index('0') # 빈칸의 인덱스 찾기(문자열에서)
        count=visited[graph_to_str]
        if graph_to_str=='123456780': #정리된 상태가 되면 
            return count #종료
        x=idx//3 # 빈칸의 행    
        y=idx%3 # 빈칸의 열

        count+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=3 or ny>=3: #이동 불가능하면
                continue

            nidx=nx*3+ny # 리스트 인덱스 다시 문자열 인덱스로 바꾸기
            graph=list(graph_to_str) #문자열을 리스트로 바꿈
            graph[nidx],graph[idx]=graph[idx],graph[nidx] #빈칸과 숫자 swap
            new_graph_to_str="".join(graph) # 리스트 다시 문자열로 만들기
            
            #새로운 문자열의 빈칸을 방문한 적이 없다면
            if visited.get(new_graph_to_str,0)==0:
                visited[new_graph_to_str]=count # 방문처리(그 동안의 이동 횟수)
                queue.append(new_graph_to_str) 
    return -1

print(bfs())


