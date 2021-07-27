import math
cnt = int(input())
input_list = []
answer = []

for i in range(cnt):
    num1, num2 = map(int, input().split())
    tmp = [num1, num2]
    input_list.append(tmp)

for chk in input_list:
    if math.gcd(chk[0], chk[1]) == 1:
        answer.append(chk[0] * chk[1])
    else:
        lcm = (chk[0] * chk[1]) // math.gcd(chk[0], chk[1])
        answer.append(lcm)

for i in answer:
    print(i)