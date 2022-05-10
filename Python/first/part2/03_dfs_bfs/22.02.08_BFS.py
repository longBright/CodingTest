# 22.02.08 BFS 알고리즘 구현

from collections import deque

def bfs(graph, start, visited):
    # 시작 위치 큐에 삽입 후 방문 처리
    q = deque([start])
    visited[start] = True
    # 큐에 데이터가 남아 있는 동안
    while q:
        # 큐에서 맨 앞 노드를 꺼냄
        head = q.popleft()       # 큐의 헤드
        print(head, end=' ')
        # 꺼낸 노드의 인접 노드 중 미방문 노드 모두를 큐에 삽입 후 방문처리
        for i in graph[head]:
            if not visited[i]:
                q.append(i)         # 노드 번호를 삽입해야함. 인덱싱을 통해 그래프로 접근 시 에러가 발생함
                visited[i] = True

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

bfs(graph, 1, visited)