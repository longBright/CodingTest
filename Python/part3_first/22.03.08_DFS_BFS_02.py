# 22.03.08 DFS/BFS 문제
# 연구소
# 못 풀었음
# 그냥 손도 못댐


n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]

for _ in range(m):
    data = list(map(int, input().split()))
    graph.append(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# dfs 를 이용해 바이러스 전파
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상 하 좌 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치 후 재귀 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 영역의 크기 계산
def get_safe():
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe

# dfs를 이용해 울타리를 설치하면서 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역 최댓값 계산
        result = max(result, get_safe())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)