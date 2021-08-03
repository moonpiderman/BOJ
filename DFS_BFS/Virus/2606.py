from collections import deque
import sys
read = sys.stdin.readline
POINT = 1

com_cnt = int(input())
connect = int(input())
lines = []
v_com = deque() # virus Computer
v_com.append(1)

for _ in range(connect):
    a, b = map(int, read().split())
    if b < a:
        a, b = b, a
    tmp = [a, b]
    lines.append(tmp)

for i in range(len(lines)):
    if lines[i][0] == POINT:
        if lines[i][1] not in v_com:
            v_com.append(lines[i][1])
    else:
        if lines[i][0] in v_com:
            if lines[i][1] not in v_com:
                v_com.append(lines[i][1])

print(len(v_com) - 1)