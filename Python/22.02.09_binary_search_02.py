# 22.02.09 이진탐색 문제
# 떡볶이 떡 만들기

# input
n, m = list(map(int, input().split()))

array = list(map(int, input().split()))
array.sort()

start = 0
end = max(array)
h = 0
while start <= end:
    mid = (start + end) // 2
    # 떡 자르기
    temp = 0
    for i in array:
        if (i - mid) < 0:
            temp += 0
        else:
            temp += i-mid
    # 자른 후의 합이 m 과 같은 값이고 이전 높이보다 클 경우
    if temp == m and mid >= h:
        h = mid
        break
    # 자른 후의 합이 m 보다 크면 우측 탐색
    elif temp > m:
        start = mid + 1
    # 자른 후의 합이 m 보다 작으면 좌측 탐색
    else:
        end = mid - 1
print(h)

# 더 좋은 코드로 변환
start = 0
end = max(array)
h = 0
while start <= end:
    mid = (start + end) // 2
    # 떡 자르기
    temp = 0
    for i in array:
        if (i - mid) >= 0:
            temp += i-mid

    # 자른 후의 합이 m 보다 작으면 좌측 탐색
    if temp < m:
        end = mid -1
    # 자른 후의 합이 m 과 같은 값이고 이전 높이보다 클 경우 우측 탐색
    # 같거나 같을 경우이므로 코드 단축
    else:
        h = mid
        start = mid + 1
print(h)