# 2021.12.27 Greedy Algorithm Exercise
# 숫자 카드 게임 p.96
# N X M 형태로 놓인 숫자 카드들 중 각 행에서의 최소값을 가지는 카드들을 고르고 그들 중 최댓값을 찾는 문제
# N : 행의 수 M : 열의 수
# 출력 : 찾은 최댓값

# N >= 1, M <= 100

# 방법 1) min, max 함수를 통한 구현

# N, M 입력
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(min_val, result)
print(result)