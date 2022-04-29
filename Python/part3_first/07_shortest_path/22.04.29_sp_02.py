# 22.04.29 최단경로 문제
# 정확한 순위
# 플로이드 워셜 알고리즘 수행까지는 접근했음
# 이후 과정은 답안 설명 참고 후 수행하였음

INF = 1e9

# n : 학생들의 수    m : 두 학생의 성적 비교 횟수
n, m = map(int, input().split())

# 그래프 생성 및 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1     # 비용은 1로 책정

# 플로이드 워셜 알고리즘 수행
# 점화식 : D[a,b] = min(D[a,b], D[a,k] + D[k,b])
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 알고리즘 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(-1, end=' ')
        else:
            print(f'{graph[a][b]:>2}', end=' ')
    print()

# a -> b 이거나 b -> a 이면 연결이 됐다고 생각
# 모든 노드와 연결이 됐으면(연결된 노드 수가 n 개 이면) 정확한 순위 파악이 가능함
result = 0
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            cnt += 1
        if cnt == n:
            result += 1
print(result)
