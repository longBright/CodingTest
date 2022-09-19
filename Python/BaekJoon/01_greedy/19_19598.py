# 22.05.18 19598번
# 최소 회의실 개수

import sys
import heapq
input = sys.stdin.readline

# 입력
n = int(input())
data = []
for _ in range(n):
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
