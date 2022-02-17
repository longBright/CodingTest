# 22.02.11 최단 경로 플로이드-워셜 알고리즘 구현

INF = int(1e9)

# 노드의 개수 및 간선 입력
n = int(input())
m = int(input())

# 그래프 생성, 모든 값을 INF 로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c     # 유향 그래프 기준
    # graph[b][a] = c   # 무향 그래프의 경우 이 코드 포함해야함

# 플로이드 워셜 알고리즘 수행
# 점화식 : D[a][b] = min(D[a][b], D[a][k] + D[k][b])
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 INFINTY 출력
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=' ')
    print()