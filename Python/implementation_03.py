# 2021.01.04 Implementation Exercise
# 예제 4-3 왕실의 나이트 - p.115

# 시작 위치 입력
input = input()

# 시작 행
row = int(input[1])
# 시작 열
col = int(ord(input[0]) - ord('a') + 1)

cnt = 0
if row + 2 <= 8 and col + 1 <= 8:
    cnt += 1
if row + 2 <= 8 and col - 1 >= 1:
    cnt += 1
if row - 2 >= 1 and col + 1 <= 8:
    cnt += 1
if row -2 >= 1 and col + 1 <= 8:
    cnt += 1
if row + 1 <= 8 and col + 2 <= 8:
    cnt += 1
if row + 1 <= 8 and col -2 >= 1:
    cnt += 1
if row - 1 >= 1 and col + 2 <= 8:
    cnt += 1
if row - 1 >= 1 and col - 2 >= 1:
    cnt += 1
print(cnt)        