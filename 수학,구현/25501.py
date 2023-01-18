def recursion(s,l,r):
  global count
  if l>=r:
    return 1
  elif s[l]!=s[r]:
    return 0
  else:
    count+=1
    return recursion(s,l+1,r-1)

def isPalindrome(s):
  return recursion(s,0,len(s)-1)

t=int(input())
for i in range(t):
  s=input()
  count=1
  print(isPalindrome(s),count)