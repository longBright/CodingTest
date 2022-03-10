# 22.03.08 DFS/BFS 문제
# 연구소

def dfs(graph, v, visited):
    visited[v] = True       # 방문 처리
    print(v, end=' ')       # 출력(동작)
    # 노드 V 에 연결된 모든 노드에 대하여
    for i in graph[v]:
        # 미방문 노드인 경우
        if not visited[i]:
            dfs(graph, i, visited)
            
n, m = map(int, input().split())
graph = []
temp = graph.copy()

for _ in range(m):
    data = list(map(int, input().split()))
    graph.append(data)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            temp[i][j] = 1