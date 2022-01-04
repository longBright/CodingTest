# 2021.01.04 Implementation Exercise
# 예제 4-4 게임 개발 - p.118

# N, M 을 공백으로 구분하여 입력
n , m = map(int, input().split())

# 방문한 위치 저장을 위한 2차원 리스트
visit_list = [[0] * m for _ in range(n)]

# 현재 캐릭터의 좌표 및 바라보는 방향 입력
x, y, direction = map(int, input().split())
visit_list[x][y] = 1        # 현재 좌표 방문 처리

# 전체 맵 정보 입력
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전 메소드
def turn_left():
    global direction
    # 왼쪽으로 회전
    direction -= 1
    # 북쪽을 보고 있을 경우 서쪽으로 설정
    if direction == -1:
        direction = 3
        
# 시뮬레이션 시작
cnt = 1     # 방문한 칸 개수
turn = 0    # 회전 횟수
while True:
    # 왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전 이후 정면에 가보지 않은 칸이 있는 경우
    if visit_list[nx][ny] == 0 and arr[nx][ny] == 0:
        visit_list[nx][ny] = 1
        x = nx; y = ny;
        cnt += 1
        turn = 0
        continue
    # 회전 후 정면 칸을 가보았거나 바다인 경우
    else:
        turn += 1       # 회전
        
    # 네 방향 모두 진행 불가능
    if turn == 4:
        nx = x - dx[direction]
        ny = x - dy[direction]
        
        # 뒤로 이동이 가능할 경우
        if arr[nx][ny] == 0:
            x = nx; y = ny;
        # 뒤로 이동이 불가능할 경우
        else:
            break
        turn = 0

print(cnt)