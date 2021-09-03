length = int(input())
li = list(map(int, (input().split())))
l = sorted(li)
total = 0
total_list = []

for i in range(length):
    total = total + l[i]
    total_list.append(total)

print(sum(total_list))