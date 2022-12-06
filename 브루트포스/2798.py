from itertools import combinations
n,m=map(int,input().split())
cards=list(map(int,input().split()))
card=list(combinations(cards,3))
new_card=[]
for i in card:
    if sum(i)<=m:
        new_card.append(sum(i))
print(max(new_card))

