# BFS 메소드
# graph : 그래프, start : 시작 노드, visited : 방문처리용 리스트

from collections import deque as dq

def bfs(graph, start, visited):
    # Queue 선언 및 시작 노드 방문처리
    q = dq([start])
    visited[start] = True
    # 큐가 빌 때 까지 진행
    while q:
        # 맨 처음 노드 제거
        v = q.popleft()
        print(v, end=' ')
        # 현재 노드와 연결된 모든 노드에 대해서 처리
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
# 그래프
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

# 방문처리용 리스트
visited = [False] * 9

bfs(graph, 1, visited)