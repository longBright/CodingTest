# 22.04.29 최단경로 문제
# 화성 탐사
# 다익스트라 알고리즘 적용(한점에서 다른 한점까지의 최소 비용 계산)
import heapq


# 다익스트라 알고리즘
def dijkstra(x, y, dist):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    dist[x][y] = graph[x][y]

    while q:
        distance, now_x, now_y = heapq.heappop(q)
        if dist[now_x][now_y] < distance:
            continue
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = distance + graph[nx][ny]
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    return dist


INF = 1e9
for _ in range(int(input())):
    n = int(input())
    dist = [[INF] * n for _ in range(n)]

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    dist = dijkstra(0, 0, dist)  # 다익스트라 알고리즘 수행. [0][0] 에서 출발.
    print(f'dist[n-1][n-1] : {dist[n-1][n-1]}')
