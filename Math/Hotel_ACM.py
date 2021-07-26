def hotel(arr):
    h, w, n = arr[0], arr[1], arr[2]
    floor = (n % h)
    width = (n // h) + 1
    if floor == 0:
        floor = h
        width -= 1
    print(floor * 100 + width)

if __name__ == '__main__':
    test_cnt = int(input())
    test_case = []
    for i in range(test_cnt):
        tmp = []
        h, w, n = map(int, input().split())
        tmp.append(h)
        tmp.append(w)
        tmp.append(n)
        test_case.append(tmp)

    for i in range(test_cnt):
        hotel(test_case[i])