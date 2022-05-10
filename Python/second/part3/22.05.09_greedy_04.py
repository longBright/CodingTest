# 22.05.09 그리디 기출 문제
# 만들 수 없는 금액

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 1
for x in data:
    if result < x:
        break
    result += x
print(result)
