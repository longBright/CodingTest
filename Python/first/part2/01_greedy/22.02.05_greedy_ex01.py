# 22.02.05 그리디 알고리즘 예제
# 동전 거스름돈 문제
# 동전 종류 - 500 100 50 10

# input money
money = int(input())
coins = [500, 100, 50, 10]

result = 0

for coin in coins:
    result += money // coin
    money %= coin

print(result)