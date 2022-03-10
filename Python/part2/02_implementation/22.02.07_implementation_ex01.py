# 22.02.07 구현 연습문제 1번
# 상하좌우

# input
n = int(input())
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            pos_x = x + dx[i]
            pos_y = y + dy[i]
    if pos_x < 1 or pos_x > n or pos_y < 1 or pos_y > n:
        continue
    # 이동
    x, y = pos_x, pos_y
    
print(x, y)