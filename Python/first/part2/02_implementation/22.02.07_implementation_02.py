# 22.02.07 구현
# 게임 개발 문제

# input
from re import T


n, m = map(int, input().split())            # 맵의 크기. n x m
x, y, d = map(int, input().split())         # 시작 위치, 방향

visited = [[0] * m for i in range(n)]       # 방문 정보 리스트
visited[x][y] = 1                           # 시작 위치 방문처리

# 맵 생성
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1     # 시작 위치도 방문 횟수에 포함
turn_time = 0
while(True): 
    if d == -1:
        d = 3
    else:
        d -= 1
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 회전 후 방문 가능 시
    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        x, y = nx, ny
        visited[x][y] = 1
        cnt += 1
        turn_time = 0
        continue
    # 회전 후 방문 불가 시
    else:
        turn_time += 1
    # 회전 완료 후에도 방문 불가 시
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dx[d]
        # 뒤로 갈 수 있으면 뒤로 이동
        if arr[nx][ny] == 0:
            x = ny
            y = nx
        # 뒤로 갈 수 없으면 종료
        else:
            break
        turn_time = 0
print(cnt)

# 최초 구현 시 turn_time 관련 코드 미작성
# turn_time 이 포함된 코드 제외하고 전부 작성 성공
# 방향 회전 시 좌측으로 회전해야 하므로 d -= 1 을 해줘야하는데
# d += 1로 해주어서 결과를 제대로 출력하지 못하는 문제점이 발생하였음
