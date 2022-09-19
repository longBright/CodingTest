# 22.05.16 16953번
# A -> B
# 틀렸음
import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 0

while True:
    if a == b:
        print(cnt + 1)
        break
    elif b < a or (b % 2 != 0 and b % 10 != 1):
        print(-1)
        break

    if b % 2 == 0:
        b //= 2
        cnt += 1
    elif b % 10 == 1:
        b //= 10
        cnt += 1

# while True:
#     if a >= b:
#         break
#     if b % (a * 10 + 1) != 0:
#         a *= 2
#         cnt += 1
#     a = a * 10 + 1
#     cnt += 1
#
# if a == b:
#     print(cnt + 1)
# else:
#     print(-1)