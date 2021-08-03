from sys import stdin
read = stdin.readline
POINT = 1

dic = {}

for i in range(int(read())):
    dic[i + 1] = set()

for _ in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

print(dic)

def DFS(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            DFS(i, dic)

visited = []
DFS(POINT, dic)
print(len(visited) - 1)
