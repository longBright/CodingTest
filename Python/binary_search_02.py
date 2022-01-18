# 22.01.18 떡볶이 떡 만들기
# 손님이 요청한 길이가 M 일 때, 최소 M 만큼(M 이상의) 떡을 손님이 받을 수 있는
# 절단기의 최댓값 구하기

# 절단기의 길이 : mid - mid 가 크면 총 길이가 짧아짐
# mid 가 작아지면 총 길이가 길어짐
# 총 길이가 요청 길이보다 짧으면 덜 잘라야함(mid의 크기가 줄어들어야함)
# 총 길이가 요청 길이보다 길면 더 잘라야함(mid 의 크기가 커져야함)

# n, m 입력
n, m = list(map(int, input().split(' ')))

# 떡의 개별 높이 입력
array = list(map(int, input().split()))
array.sort()

start = 0
end = max(array)
# 이진 탐색을 통해 최적의 절단기 높이 탐색
ans = None
while(start <= end):
    mid = (start + end) // 2
    total = 0
    # 잘랐을 때의 떡의 총 길이 계산
    for i in array:
        if i > mid:
            temp = i - mid
            total += temp
    # 총 길이가 부족한 경우 더 많이 절단(왼쪽 탐색)
    if total < m:
        end = mid - 1
    # 총 길이가 길 경우 덜 절단(오른쪽 탐색)
    else:
        ans = mid   # 최대한 덜 절단한 경우가 정답임
        start = mid + 1
        
print(ans)