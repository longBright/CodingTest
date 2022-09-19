# 22.05.28 1715번
# 카드 정렬하기
# 파일 합치기와 동일한 문제
import heapq

k = int(input())
q = []
for i in range(k):
    q.append(int(input()))
heapq.heapify(q)

result = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a + b
    heapq.heappush(q, a + b)
print(result)
