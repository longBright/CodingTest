from collections import deque

def sol(x, y, graph):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        # 상 하 좌 우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 벗어난 경우
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            # 장애물이 있는 경우
            if graph[nx][ny] == 0:
                continue
            # 장애물이 없는 경우 최단 거리 추가
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n-1][m-1]

# N, M
n, m = map(int, input().split())

# 그래프 초기화
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 위치 : 0, 0
ans = sol(0, 0, graph)
print(ans)