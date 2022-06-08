# 22.06.08 구현 문제
# 게임 개발

def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction


n, m = map(int, input().split())
x, y, d = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
array[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1
turn_cnt = 0
while True:
    d = turn_left(d)
    nx = x + dx[d]
    ny = y + dy[d]
    if array[nx][ny] == 0:
        x, y = nx, ny
        array[x][y] = 1
        cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        nx = x - dx[d]
        ny = y - dx[d]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_cnt = 0
print(cnt)