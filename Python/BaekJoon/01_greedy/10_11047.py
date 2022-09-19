# 22.05.14 11047번
# 동전 0

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

result = 0
for coin in coins:
    result += k // coin
    k %= coin
print(result)
