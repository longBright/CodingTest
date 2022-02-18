# 22.02.18 Part 3 그리디 문제
# 볼링공 고르기

n, m = map(int, input().split())
k = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        if k[i] != k[j]:
            result += 1
print(result)


# 교재 예시 답안
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
    array[x] += 1
    
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)