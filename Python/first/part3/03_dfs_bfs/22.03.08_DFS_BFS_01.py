# 22.03.08 DFS/BFS 문제
# 특정 거리의 도시 찾기

from collections import deque
from math import dist

def bfs(graph, start, distance):
    # 시작 위치 큐에 삽입 후 방문 처리
    q = deque([start])
    # 큐에 데이터가 남아 있는 동안
    while q:
        # 큐에서 맨 앞 노드를 꺼냄
        head = q.popleft()       # 큐의 헤드
        # 꺼낸 노드의 인접 노드 중 미방문 노드 모두를 큐에 삽입 후 방문처리
        for i in graph[head]:
            if distance[i] == -1:
                q.append(i)         # 노드 번호를 삽입해야함. 인덱싱을 통해 그래프로 접근 시 에러가 발생함
                distance[i] = distance[head] + 1

def sol(n, graph, start, distance, target):
    bfs(graph, start, distance)
    if target in distance:
        for i, dist in enumerate(distance):
            if dist == target: print(i)
    else:
        print(-1)

n, m, k, x = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]
distance = [-1] * (n+1)
distance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
sol(n, graph, x, distance, k)