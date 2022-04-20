# 22.04.20 이진 탐색 문제
# 고정점 찾기

def sol(data, n):
    left = 0
    right = n-1
    
    while(left<=right):
        mid = (left+right) // 2
        if mid == data[mid]:
            return mid
        elif mid < data[mid]:
            right = mid
        else:
            left = mid
    return -1

n = int(input())
data = list(map(int, input().split()))

print(sol(data, n))