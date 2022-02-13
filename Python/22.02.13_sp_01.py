# 22.02.13 최단 경로 문제
# 미래도시

INF = int(1e9)
# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())

# N x N 그래프 생성
graph = [[INF] * (n+1) for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 최종 목표와 경유지 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1번에서 출발하여 K를 거쳐 X 까지 가는 비용
dist = graph[1][k] + graph[k][x]

if dist >= INF:
    print("-1")
else:
    print(dist)