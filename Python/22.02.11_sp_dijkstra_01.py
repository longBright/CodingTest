# 22.02.11 최단 경로 다익스트라 알고리즘 구현
# 간단한 구현 => sp_dijkstra_02.py : 개선된 구현

from platform import java_ver
import sys
input = sys.stdin.readline
INF = int(1e9)  # 10억

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
    graph[a].append((b,c))      # a 노드에서 b 노드로 가는 비용이 c
    
# 미방문 노드 중, 최단 거리 노드 번호 반환
def get_shortest_node():
    min_val = INF
    index = 0       # 최단 거리 노드
    for i in range(1, n+1):
        if dist[i] < min_val and not visited[i]:
            min_val = dist[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    dist[start] = 0
    visited[start] = True
    # 시작 노드와 연결된 노드까지의 거리 초기화
    for i in graph[start]:
        dist[i[0]] = i[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리 노드를 꺼내서 방문 처리
        temp = get_shortest_node()
        visited[temp] = True
        # 현재 노드(temp) 와 연결된 다른 노드 확인
        for j in graph[temp]:
            cost = dist[temp] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[j[0]]:
                dist[j[0]] = cost
                
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