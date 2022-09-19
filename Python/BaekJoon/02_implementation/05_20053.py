# 22.06.13 20053번
# 최소, 최대2
T = int(input())
while T:
    n = int(input())
    data = list(map(int, input().split()))
    print(min(data), max(data))
    T -= 1
