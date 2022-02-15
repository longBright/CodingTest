# 22.02.15 그래프 이론 - 위상 정렬
from collections import deque
# 위상 정렬
def topology_sort(graph, indegree, v):
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print(result)
    
# 노드, 간선 개수 입력
v, e = map(int, input().split())

# 진입 차수 테이블 초기화 및 간선 정보 입력
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort(graph, indegree, v)