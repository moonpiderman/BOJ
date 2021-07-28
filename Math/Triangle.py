import math
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    tmp = [a, b, c]
    tmp = sorted(tmp)
    if math.pow(tmp[2], 2) == (math.pow(tmp[0], 2) + math.pow(tmp[1], 2)):
        print('right')
    else:
        print('wrong')