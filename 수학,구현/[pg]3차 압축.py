from string import ascii_uppercase
msg='KAKAO'
msg2='KAKAO'
answer=[]
alphabet = {}
for i in range(len(ascii_uppercase)):
	alphabet[ascii_uppercase[i]] = i+1
for k in range(len(msg)):
  for i in range(len(msg),-1,-1):
    if msg[k:i] in alphabet:
      answer.append(alphabet[msg[k:i]])
      alphabet[msg2[k:i+1]]=len(alphabet)+1
      msg2=msg[i:]
      print(msg2)
      break
print(alphabet)
print(answer)
