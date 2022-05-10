# 22.05.09 그리디 문제
# 숫자 카드 게임

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

result = 0
for i in range(n):
    result = max(result, min(data[i]))
print(result)