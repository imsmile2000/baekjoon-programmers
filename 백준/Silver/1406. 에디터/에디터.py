import sys
start = list(sys.stdin.readline().rstrip())
m = int(input())
start2 = []
for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'L' and start:
        start2.append(start.pop())
    elif command[0] == 'D' and start2:
        start.append(start2.pop())
    elif command[0] == 'B' and start:
        start.pop()
    elif command[0] == 'P':
        start.append(command[1])
print(''.join(start+list(reversed(start2))))
 