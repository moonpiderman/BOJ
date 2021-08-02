from collections import deque

m, n, k = map(int, input().split())
frame = [list(0 for _ in range(n)) for _ in range(m)]

for _ in range(k):
    x_s, y_s, x_e, y_e = map(int, input().split())
    for i in range(m - y_e, m - y_s):
        for j in range(x_s, x_e):
            frame[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(i, j):
    queue = deque([[i, j]])
    frame[i][j] = 1
    cnt = 1
    while queue:
        now = queue.popleft()
        x, y = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1 :
                continue
            if frame[nx][ny] == 0:
                queue.append([nx, ny])
                frame[nx][ny] = 1
                cnt += 1
    return cnt

area = 0
cnts = []
for i in range(m):
    for j in range(n):
        if frame[i][j] == 0:
            cnts.append(BFS(i, j))
            area += 1
print(area)
cnts.sort()
print(*cnts)