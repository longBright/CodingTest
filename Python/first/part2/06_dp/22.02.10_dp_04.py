# 22.02.10 다이나믹 프로그래밍
# 효율적인 화폐 구성

# INF
INF = 999999

# input
n, m = list(map(int, input().split()))

coins = []
for _ in range(n):
    coins.append(int(input()))

d = [INF] * (m+1)
d[0] = 0

for coin in coins:
    for i in range(coin, m+1):
        d[i] = min(d[i], d[i-coin] + 1)
        

# for coin in coins:
#     for i in range(coin, m+1):
#         if d[i - coin] != INF:            # if 문을 추가해서 불필요한 연산을 방지
#             d[i] = min(d[i], d[i-coin] + 1)
        
if d[m] == INF:
    print(-1)
else:
    print(d[m])