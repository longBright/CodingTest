# 22.05.25 2414번
# 우체국

# 정답 코드
import sys
input = sys.stdin.readline


N = int(input())
postOffice = [list(map(int, input().split())) for _ in range(N)]

postOffice.sort(key=lambda x: x[0])
mid = round(sum(p for _, p in postOffice)/2)

pCount = 0
for i, p in postOffice:
    pCount += p

    if pCount >= mid:
        print(i)
        break

# 시간 초과
# import sys
#
# input = sys.stdin.readline
# n = int(input())
#
# X = []
# A = []
# for i in range(n):
#     x, a = map(int, input().split())
#     X.append(x)
#     A.append(a)
#
# distance = [0] * n
# for i in range(n):
#     distance[i] = sum(A[:i]) + sum(A[i+1:])
# result = distance.index(min(distance)) + 1
# print(result)
