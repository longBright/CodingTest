# 22.05.12 1758번
# 알바생 강호
# https://www.acmicpc.net/problem/1758

N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
data.sort(reverse=True)

result = 0
for i in range(N):
    if data[i] - i < 0:
        continue
    result += data[i] - i
print(result)
