from collections import deque
import sys
read = sys.stdin.readline

def BFS(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

def DFS(v):
    visit_list2[v] = 1
    print(v, end=' ')
    for i in range(1, n + 1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            DFS(i)
# n : 정점의 갯수
# m : 간선의 갯수
# v : 탐색을 시작할 정점
n, m, v = map(int, read().split())

# 인덱스와 값을 일치시키기 위해서 n + 1 크기의 행렬을 만들어준다.
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, read().split())
    # 양방향 간선에 1
    graph[a][b] = graph[b][a] = 1

DFS(v)
print()
BFS(v)
