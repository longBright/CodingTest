# 2022.01.18 이진탐색
# 부품찾기

# 이진탐색 메소드
def sol(array, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        # 일치하는 경우 반환
        if array[mid] == target:
            return mid
        # mid 의 좌측 탐색
        elif array[mid] > target:
            end = mid - 1
        # mid 의 우측 탐색
        else:
            start = mid + 1
    return None     # 없으면 None 반환

# input n, m, list
n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
m_list = list(map(int, input().split()))

# 요청 품목이 있을 경우 yes 출력
# 요청 품목이 없을 경우 no 출력
for i in m_list:
    ans = sol(array, i, 0, n-1)
    if ans != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')