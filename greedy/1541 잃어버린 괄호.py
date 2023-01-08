import sys
import re
expression=sys.stdin.readline().rstrip()
num=re.split('[-+]',expression)
oper=re.findall('[-+]',expression)
for i in range(len(oper)-1):
    if oper[i]=='-':
        oper[i+1:]='-'  #-가 있으면 그 이후의 숫자들은 다 빼줌 괄호쳐주는 것과 같은 원리
result=int(num[0])
for i in range(1,len(num)):
    if oper[i-1]=='+':
        result+=int(num[i])
    else:
        result-=int(num[i])
print(result)