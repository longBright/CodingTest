# 22.02.18 Part 3 그리디 문제
# 만들 수 없는 금액
# 못 풀었음

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin
print(target)