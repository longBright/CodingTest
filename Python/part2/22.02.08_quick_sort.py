# 22.02.08 퀵 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 가장 널리 사용되는 직관적인 형태의 퀵 정렬
# start : 시작 인덱스, end : 마지막 인덱스
def q_sort(arr, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start       # 피벗은 첫번째 원소로 지정
    left = start + 1
    right = end
    
    while left <= right:
        # 피벗보다 큰 원소를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        # 엇갈린 경우 작은 데이터와 피벗을 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않은 경우 작은 데이터와 큰 데이터 스왑
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    q_sort(arr, start, right - 1)
    q_sort(arr, right + 1, end)

q_sort(arr, 0, len(arr) - 1)
print(arr)


# 파이썬의 장점을 살린 간결한 퀵 정렬


def py_q_sort(arr):
    # 원소가 하나 이하이면 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # 피벗은 첫번째 원소
    tail = arr[1:]  # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot]     # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot]     # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행 후, 전체 리스트 반환
    return py_q_sort(left_side) + [pivot] + py_q_sort(right_side)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

arr = py_q_sort(arr)
print(arr)