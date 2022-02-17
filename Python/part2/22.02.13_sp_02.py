# 22.20.13 최단 경로 문제
# 전보
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(c)

cnt = 0
max_dist = 0
for dist in distance:
    if dist != INF and dist != 0:
        cnt += 1
    if dist != INF and dist > max_dist:
        max_dist = dist
        
print(cnt, max_dist)

# 출력부는 아래와 같이 수정 가능
cnt = 0
max_dist = 0
for dist in distance:
    if dist != INF:
        cnt += 1
        max_dist = max(max_dist, dist)
print(cnt-1, max_dist)