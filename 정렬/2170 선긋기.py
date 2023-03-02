import sys
n=int(sys.stdin.readline())
line=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    line.append((x,y))
line.sort(key=lambda x:(x[0],x[1])) # sort

start=line[0][0] #start
end=line[0][1] #end
count=0 # 선의 길이


for i in range(1,n):
    if start<=line[i][0]<=end and line[i][1]>end: # 선의 시작이 start와 end 사이에 있고 선의 끝이 end보다 크면
        end=line[i][1] # end를 수정
    elif line[i][0]>end: # 선의 시작이 end보다 크면 
        count+=end-start # count+=선의 길이
        start=line[i][0] # start 수정
        end=line[i][1] # end 수정
print(count+end-start)
    

    