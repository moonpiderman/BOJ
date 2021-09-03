from collections import deque
cnt, how = map(int, input().split())
coin_list = []
count_coin = 0

for i in range(cnt):
    coin_list.append(int(input()))
coin_list = deque(sorted(coin_list, reverse=True))

while coin_list:
    chk = coin_list.popleft()
    if how != 0:
        if chk > how:
            continue
        else:
            # 반복문 넣어서 몫, 나머지로 변형시키기 ex) how = xxxx % n
            count_coin += how // chk
            how = how % chk
    else:
        continue

print(count_coin)