# 22.05.09 그리디 문제
# 큰수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

cnt = 1
result = 0
for _ in range(m):
    if cnt == k:
        result += data[-2]
        cnt = 1
    else:
        result += data[-1]
        cnt += 1
print(result)
