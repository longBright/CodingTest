# 22.05.28 13975번
# 파일 합치기

# 우선 순위 큐 적용 -> 시간 초과 해결
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)

    result = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a + b
        heapq.heappush(q, a+b)
    print(result)


# 시간 초과
# T = int(input())
# for _ in range(T):
#     k = input()
#     data = list(map(int, input().split()))
#     data.sort(reverse=True)
#     result = 0
#     while len(data) > 1:
#         a = data.pop()
#         b = data.pop()
#         data.append(a+b)
#         data.sort(reverse=True)
#         result += a+b
#     print(result)
