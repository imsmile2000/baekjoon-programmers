def solution(bandage, health, attacks):
    attack_time=[]
    attack=[]
    for x,y in attacks:
        attack_time.append(x)
        attack.append(y)
    hp=health
    cnt=0
    for i in range(1,max(attack_time)+1):
        if i not in attack_time:
            cnt+=1
            if cnt==bandage[0]:
                hp+=bandage[2]
                cnt=0
            hp+=bandage[1]
            if hp>health:
                hp=health
        else:
            hp-=attack[0]
            attack.pop(0)
            cnt=0
        if hp<=0:
            hp=-1
            break
    return hp