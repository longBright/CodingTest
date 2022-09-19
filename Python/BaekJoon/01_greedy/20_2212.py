# 22.05.18 2212번
# 센서

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = list(map(int, input().split()))
data.sort()

dist = []
for i in range(n-1):
    dist.append(data[i+1] - data[i])
dist.sort()
print(sum(dist[:n-k]))
