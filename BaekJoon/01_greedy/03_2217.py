# 22.05.11 2217번
# 로프
# https://www.acmicpc.net/problem/2217

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

for w in range(10000):
    if w // n >= min(data):
        break
print(w)


data.sort(reverse=True)
#result = []
result = 0
for i in range(n):
    #result.append(data[i]*(i+1))
    result = max(result, data[i]*(i+1))
#print(max(result))
