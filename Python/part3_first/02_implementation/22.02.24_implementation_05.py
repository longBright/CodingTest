# 22.02.24 구현 문제
# 뱀
# 틀림

# 방향 전환
def turn(c):
    global direction
    # 좌측 회전
    if c == 'L':
        direction -= 1
        if direction == -1:
            direction = 3
    # 우측 회전
    elif c == 'D':
        direction += 1
        if direction == 4:
            direction = 0

n = int(input())    # 맵의 크기
k = int(input())    # 사과의 개수

# 맵 생성
graph = [[0] * (n+1) for _ in range(n+1)]
graph[1][1] = 2     # 뱀 시작 위치

# 사과 위치 입력
for _ in range(k):
    row, col = map(int, input().split())
    graph[row][col] = 1

# 방향 변환 횟수
l = int(input())

# 방향 변환 정보 리스트
info =[]
# 방향 변환 입력
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 하단부 : 시뮬레이션 부분(본 프로그램의 주요 루틴)
# 교재 예시 답안과 다른 점
# 교재 예시 답안 : if 조건부를 이동 가능한 경우로 설정
# 작성 답안 : if 조건부를 이동 불가능한 경우로 설정 => 문제 없었음


# 교재 예시 답안 : 큐를 사용하였음
# 작성 답안 : 큐 미사용 --- 꼬리와 머리 구현을 위해 큐를 사용해야함 => 이거 때문에 틀림
result = 0
direction = 0
x, y = 1, 1
i = 0       # 방향 변환 인덱스
q = [(x, y)]
while(True):
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 범위를 벗어난 경우
    if nx > n or nx < 1 or ny > n or ny < 1 or graph[nx][ny] == 2:
        result += 1
        break
    else:
        # 다음칸에 사과가 있는 경우
        if graph[nx][ny] == 1:
            graph[nx][ny] = 2
            q.append((nx, ny))
        # 사과가 없는 경우
        else:
            graph[nx][ny] = 2   # 머리 이동
            q.append((nx, ny))
            px, py = q.pop(0)
            graph[px][py] = 0
    result += 1     # 시간 증가
    x, y = nx, ny       # 위치 이동
    # 회전 시간이 되었을 경우(i 가 l 보다 작아야하는 조건을 빠트렸었음)
    if i < l and result == info[i][0]:
        turn(info[i][1])
        i+=1
print(result)