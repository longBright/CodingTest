# 22.02.08 BFS 문제
# 미로탈출

from collections import deque

# BFS 메소드
def bfs(x, y):
    # 시작 노드 큐 삽입
    q = deque()
    q.append((x, y))
    # 큐가 빌 때까지
    while q:
        x, y = q.popleft()      # 큐에서 현재 노드 제거
        # 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # out of range
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 이동 불가
            if graph[nx][ny] == 0:
                continue
            # 이동 가능
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1     # 이전 노드의 거리의 값 + 1 => 현재 노드까지 거리의 값
                q.append((nx, ny))                  # 큐에 현재 노드 추가
    return graph[n-1][m-1]      # 그래프의 n, m 노드 값 출력 (0번 인덱스부터 시작 => -1을 해줘야함)

# input
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))