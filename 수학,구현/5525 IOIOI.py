n=int(input())
m=int(input())
s=input()
i=0
count=0
answer=0
while i<m-1: #문자열의 길이-2 만큼 (i+=2 해줄거기때문)
    if s[i:i+3]=='IOI': #P[1]='IOI'
        i+=2 
        count+=1 
        if count==n: #P[n]이 되면
            answer+=1 # P[n]의 개수 count
            count-=1
    else: #IOI가 아니라면
        i+=1 # index + 1
        count=0 # count 초기화

print(answer)
