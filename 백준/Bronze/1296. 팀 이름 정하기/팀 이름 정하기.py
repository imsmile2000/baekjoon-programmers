yeondoo=input()
n=int(input())
teams=[]
for i in range(n):
    teams.append(input())
dic={}
answer=[]
L,O,V,E=0,0,0,0
for team in teams:
    L=team.count('L')+yeondoo.count('L')
    O+=team.count('O')+yeondoo.count('O')
    V+=team.count('V')+yeondoo.count('V')
    E+=team.count('E')+yeondoo.count('E')
    score=((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    answer.append(score)
    L,O,V,E=0,0,0,0
if len(set(answer))==n:
    print(teams[answer.index(max(answer))])
else:
    answers=[]
    for i in range(n):
        if answer[i]==max(answer):
            answers.append(teams[i])
    answers.sort()
    print(answers[0])