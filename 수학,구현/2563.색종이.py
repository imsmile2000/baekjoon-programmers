def compute_intersect_area(rect1, rect2):
    
    x1, y1 = rect1[0], rect1[1] 
    x2, y2 = rect1[0]+10, rect1[1]+10
    x3, y3 = rect2[0], rect2[1] 
    x4, y4 = rect2[0]+10, rect2[1]+10

    ## case1 오른쪽으로 벗어나 있는 경우
    if x2 < x3:
        return 0
    ## case2 왼쪽으로 벗어나 있는 경우
    if x1 > x4:
        return 0
    ## case3 위쪽으로 벗어나 있는 경우
    if  y2 < y3:
        return 0
    ## case4 아래쪽으로 벗어나 있는 경우
    if  y1 > y4:
        return 0

    left_up_x = max(x1, x3)
    left_up_y = max(y1, y3)
    right_down_x = min(x2, x4)
    right_down_y = min(y2, y4)

    width = right_down_x - left_up_x
    height =  right_down_y - left_up_y
  
    return width * height

n=int(input())
paper=[]
for i in range(n):
  x,y=map(int,input().split())
  paper.append((x,y))
paper.sort()