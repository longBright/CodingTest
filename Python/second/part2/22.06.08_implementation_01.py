# 22.06.08 구현 문제
# 상하좌우

n = int(input())
plans = list(input().split())

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = y = 1
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나지 않으면 이동
            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny
print(x, y)
