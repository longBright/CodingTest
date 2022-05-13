# 22.05.13 11399번
# ATM

N = int(input())
P = list(map(int, input().split()))

P.sort()

result = []
total_now = 0
for i in range(N):
    total_now += P[i]
    result.append(total_now)
print(sum(result))
