# 22.04.20 이진탐색 문제
# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

data = list(map(int, input().split()))

answer = bisect_right(data, x) - bisect_left(data, x)

if answer == 0:
    print(-1)
else:
    print(answer)