def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

start, end = map(int, input().split())
arr = []

for num in range(start, end + 1):
    if prime(num):
        print(num)