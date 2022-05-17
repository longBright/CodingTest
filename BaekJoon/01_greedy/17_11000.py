# 22.05.17 11000번
# 강의실 배정
# 접근 잘함
# sys 라이브러리 미사용으로 시간 초과 발생

import heapq
import sys

input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()

q = []
heapq.heappush(q, data[0][1])
for i in range(1, n):
    if data[i][0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, data[i][1])
    else:
        heapq.heappush(q, data[i][1])
print(len(q))

# import heapq
#
# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
# data.sort(key=lambda x: (x[1], x[0]))
#
# q = []
# heapq.heappush(q, data[0])
# s, t = data[0]
# for i in range(1, n):
#     if data[i][0] >= t:
#         s, t = heapq.heappop(q)
#         heapq.heappush(q, data[i])
#     else:
#         heapq.heappush(q, data[i])
# print(len(q))
