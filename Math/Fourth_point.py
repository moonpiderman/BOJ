x_line = []
y_line = []
for i in range(3):
    x, y = map(int, input().split())
    x_line.append(x)
    y_line.append(y)

for i in range(3):
    if x_line.count(x_line[i]) == 1:
        x = x_line[i]
    if y_line.count(y_line[i]) == 1:
        y = y_line[i]
print(x, y)