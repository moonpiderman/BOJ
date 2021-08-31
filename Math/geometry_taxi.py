# 유클리드 기하학 원의 넓이 : PI * r^2
# 택시 기하학 원의 넓이 : 2 * r^2
import math

r = int(input())

u = math.pi * math.pow(r, 2)
t = 2 * math.pow(r, 2)

print("{:.6f}".format(u))
print("{:.6f}".format(t))