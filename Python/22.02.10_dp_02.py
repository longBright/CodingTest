# 22.02.10 다이나믹 프로그래밍
# 개미 전사
# 못풀었음

# input
n = int(input())

array = list(map(int, input().split()))

# dp 테이블을 통하여 구현
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d)
print(d[n-1])

# 재귀함수로 구현
def sol(k, x):
    if x == 0:
        return k[0]
    if x == 1:
        return max(k[0], k[1])
    else:
        print(max(sol(k, x-1), k[x]+k[x-2]), end=' ')
        return max(sol(k, x-1), k[x]+k[x-2])
    
result = sol(array, n-1)
print()
print(result)