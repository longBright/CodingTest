# 22.02.09 이진 탐색 문제
# 부품 찾기

# 이진탐색 메소드
def bin_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return bin_search(array, target, mid + 1, end)
    else:
        return bin_search(array, target, start, mid - 1)
# input
n = int(input())
store = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

store.sort()
for item in request:
    if bin_search(store, item, 0, n-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')