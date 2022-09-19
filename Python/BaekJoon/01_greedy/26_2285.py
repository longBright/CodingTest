# 22.05.29 2285번
# 우체국
import sys

input = sys.stdin.readline
n = int(input())

X = []
A = []
for i in range(n):
    x, a = map(int, input().split())
    X.append(x)
    A.append(a)

distance = [0] * n
for i in range(n):
    distance[i] = sum(A[:i]) + sum(A[i+1:])
result = distance.index(min(distance)) + 1
print(result)
