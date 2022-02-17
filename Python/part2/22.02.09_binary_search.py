# 22.02.09 이진탐색

# 재귀함수로 구현한 이진탐색
def recursive_binary_search(array, target, start, end):
    # 종료 조건(못 찾은 경우 None 반환)
    if start > end:
        return None
    mid = (start + end) // 2
    print("rec : ", mid, array[mid])
    # 찾을 경우 해당 중간 인덱스 값 반환
    if array[mid] == target:
        return mid
    # 중간 인덱스 값이 찾는 값보다 클 경우 좌측 부분 탐색
    elif array[mid] > target:
        return recursive_binary_search(array, target, start, mid - 1)
    # 중간 인덱스 값이 찾는 값보다 작은 경우 우측 부분 탐색
    else:
        return recursive_binary_search(array, target, mid + 1, end)

        
# 반복문으로 구현한 이진탐색
def loop_binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        print("loop :", mid, array[mid])
        # 찾을 경우 해당 중간 인덱스 값 반환
        if array[mid] == target:
            return mid
        # 중간 인덱스 값이 찾는 값보다 작은 경우 우측 부분 탐색
        elif array[mid] < target:
            start = mid + 1
        # 중간 인덱스 값이 찾는 값보다 큰 경우 우측 부분 탐색
        else:
            end = mid - 1
    # 못찾으면 None 반환
    return None
    
# 원소의 개수와 찾고자 하는 값 입력
n, target = map(int, input().split())
print(type(target))

# 전체 원소 입력
array = list(map(int, input().split()))
print(type(array[0]))

array.sort()

# 결과 출력
result1 = recursive_binary_search(array, target, 0, n - 1)
result2 = loop_binary_search(array, target)

if result1 == None:
    print(f"{target}이 존재하지 않습니다!")
else:
    print((result1 + 1))

if result2 == None:
    print(f"{target}이 존재하지 않습니다!")
else:
    print((result2 + 1))