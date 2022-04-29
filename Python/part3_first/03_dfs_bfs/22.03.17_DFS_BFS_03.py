# 22.03.17 DFS/BFS 문제
# 경쟁적 전염
# 다시 풀어봐야함
# 미방문 노드 처리를 빼먹었었음

# 입력
from collections import deque


n, k = map(int, input().split())

graph = []      # 실험관
virus = []      # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))
virus.sort()

q = deque((virus))

target_s, target_x, target_y = map(int, input().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    v, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append((v, s+1, nx, ny))      # 미방문 노드 큐에 추가
    s += 1
result = graph[target_x-1][target_y-1]
print(graph)
print(result)