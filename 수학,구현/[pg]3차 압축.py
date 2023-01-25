from string import ascii_uppercase
def solution(msg):
    answer=[]
    alphabet = {}
    for i in range(len(ascii_uppercase)):
	    alphabet[ascii_uppercase[i]] = i+1
    k=0
    i=len(msg)
    while True:
        if msg[k:i] in alphabet:
            answer.append(alphabet[msg[k:i]])
            if i>=len(msg):
                return answer
            alphabet[msg[k:i+1]]=len(alphabet)+1
            k+=len(msg[k:i])
            i=len(msg)
        else:
            i-=1