from collections import Counter
def solution(players, callings):
    player_d={player:idx for idx,player in enumerate(players)}
    for call in callings:
        i=player_d[call]
        players[i-1],players[i]=players[i],players[i-1]
        player_d[players[i]] = i
        player_d[players[i-1]] = i-1
    return players