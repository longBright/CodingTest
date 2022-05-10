# 22.04.29 최단경로 문제
# 숨바꼭질
# 다익스트라 알고리즘 적용
import heapq


# 다익스트라 알고리즘
def dijkstra(start, dist):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue

        for node in graph[now]:
            cost = distance + 1
            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(q, (cost, node))

INF = 1e9
n, m = map(int, input().split())

dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)      # 무향 그래프 -> 양방향 연결

print(graph)
# 다익스트라 알고리즘 수행
dijkstra(1, dist)

max_node = 0
max_dist = 0
result = []
for i in range(1, n+1):
    if dist[i] > max_dist:
        max_dist = dist[i]
        max_node = i
        result = [max_node]
    elif dist[i] == max_dist:
        result.append(i)
print(max_node, max_dist, len(result))
