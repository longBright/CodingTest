# 22.04.29 최단 경로 문제
# 플로이드
# 플로이드 워셜 알고리즘 적용
# 점화식 : D[a,b] = min(D[a,b], D[a,k] + D[k, b])

INF = 1e9
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로의 비용을 0 으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:     # 가장 짧은 간선의 정보만 저장(입력 조건에 의해)
        graph[a][b] = c     # 유향 그래프 => a to b 의 비용만 고려함

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()