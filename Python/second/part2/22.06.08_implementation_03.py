# 22.06.08 구현 문제
# 왕실의 나이트
start = input()
col = ord(start[0]) - ord('a') + 1    # 1부터 시작
row = int(start[1])                      # 1부터 시작
steps = [[2, 1], [2, -1], [-2, 1], [-2, -1],
         [1, 2], [1, -2], [-1, 2], [-1, -2]]

cnt = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if 1 <= nrow <= 8 and 1 <= ncol <= 8:
        cnt += 1
print(cnt)
