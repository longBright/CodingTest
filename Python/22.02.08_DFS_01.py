# 22.02.08 DFS 문제
# 음료수 얼려 먹기

# DFS 메소드
def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 얼릴 수 있는경우(graph[x][y] == 0)
    if graph[x][y] == 0:
        graph[x][y] = 1     # 방문처리
        # 상하좌우 방문
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# input
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 메인
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
print(cnt)