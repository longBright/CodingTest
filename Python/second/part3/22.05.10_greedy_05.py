# 22.05.10 그리디 기출 문제
# 볼링공 고르기
# 모범 답안은 combinations 미사용
# 모범 답안 : ../first/part3/01_greedy/22.02.18_greedy_05.py
# 사실 내가 작성한 코드는 그리디 알고리즘 사용이라고 보기엔 어려움. 편법임

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = list(combinations(data, 2))
print(result)
for x in result:
    a, b = x
    if a == b:
        result.remove(x)
print(result)
print(len(result))
