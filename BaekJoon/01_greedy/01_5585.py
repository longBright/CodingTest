# 22.05.11 5585번
# 거스름돈
# 링크 : https://www.acmicpc.net/problem/5585

money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
for coin in coins:
    cnt += (money // coin)
    money %= coin
print(cnt)
