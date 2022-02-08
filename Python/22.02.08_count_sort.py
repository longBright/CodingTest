# 22.02.08 계수정렬

# 모든 원소의 값은 0 이상의 값이라고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언
# 범위는 0 ~ 9 까지이므로 리스트의 길이는 max(arr) + 1이 되어야함
count = [0] * (max(arr) + 1)

# 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(arr)):
    count[arr[i]] += 1
    
# 리스트에 기록된 정렬 정보 확인
# 등장한 횟수만큼 해당 인덱스 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')