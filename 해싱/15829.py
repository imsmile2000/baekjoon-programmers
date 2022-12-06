import sys
l=int(sys.stdin.readline())
s=sys.stdin.readline()
M=1234567891
hash=0
for i in range(len(s)-1):
    hash+=((ord(s[i])-96)*(31**i))
print(hash%M)