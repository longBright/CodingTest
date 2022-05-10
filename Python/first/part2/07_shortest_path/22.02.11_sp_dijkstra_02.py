# 22.02.11 최단 경로 다익스트라 알고리즘 구현 2
# 이 코드를 완벽하게 구현 가능해야함 - 숙지 필요

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]        # 0번 노드는 없는 것으로 가정
# 방문 처리용 리스트
visited = [False] * (n+1)               # 역시 0번 노드는 없는 것으로 가정
# 최단거리 테이블 - INF 로 초기화
dist = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))      # a 노드에서 b 노드로 가는 비용이 c


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보
        distance, now = heapq.heappop(q)
        # 방문 노드 무시
        if dist[now] < distance:
            continue
        
        # 현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now]:            # i : 인접 노드 정보 [번호, 거리]
            cost = distance + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 갈 수 없는 경우 INFINITY 출력
    if dist[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 시작 노드에서 해당 노드까지의 거리 출력
    else:
        print(f'from {start} shortest path to {i} : {dist[i]}')