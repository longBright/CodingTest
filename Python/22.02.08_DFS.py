# 22.02.08 DFS 알고리즘 구현
def dfs(graph, v, visited):
    visited[v] = True       # 방문 처리
    print(v, end=' ')       # 출력(동작)
    # 노드 V 에 연결된 모든 노드에 대하여
    for i in graph[v]:
        # 미방문 노드인 경우
        if not visited[i]:
            dfs(graph, i, visited)


# 그래프 정보
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 노드 정보
visited = [False] * (len(graph))

dfs(graph, 1, visited)