# 22.02.07 구현
# 왕실의 나이트 문제

# input
pos = input()
row = int(pos[1])                           # 정수형으로 변환(행)
col = int(ord(pos[0])) - int(ord('a')) + 1  # a 를 1로 가정 후 정수형으로 변환(열)

# 이동 가능한 방향 정의
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

# 이동 가능한 방향들 중 가능한 이동이 있으면 카운트 증가, 없으면 다음 방향 검사
cnt = 0
for move in moves:
    nrow = row + move[0]
    ncol = col + move[1]
    if nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8:
        continue
    else:
        cnt += 1
        
print(cnt)