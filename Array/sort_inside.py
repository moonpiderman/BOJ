value = str(input())
value = list(value)

for i in range(len(value)):
    value[i] = int(value[i])

value = sorted(value, reverse=True)
for i in range(len(value)):
    print(value[i], end='')