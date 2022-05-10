# 22.02.17 그래프 이론 문제
# 커리큘럼

# 위상 정렬
from collections import deque
from copy import deepcopy


def topology_sort(n, graph, indegree, result, time):
    q = deque()
    result = deepcopy(time)
    # 최초에 진입차수가 0 인 노드 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        # 연결된 간선 제거
        for i in graph[now]:
            # 문제의 조건
            # 수강에 필요한 최소 시간 : max(현재 최소 시간 + 진입 노드 수강시간, 진입 노드의 현재 최소 시간)
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 결과 출력
    for i in range(1, n+1):
        print(result[i])
    
# 노드 개수 입력
n = int(input())

# 차수, 비용, 결과 리스트 생성
indegree = [0] * (n+1)
time = [0] * (n+1)
result = []

# 그래프 생성
graph = [[] for _ in range(n+1)]

# 간선 정보 입력
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]       # 입력된 시간은 0번 인덱스
    # 1번 인덱스 ~ 마지막 직전 인덱스까지는 해당 노드가 진입하는 노드
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1
        
# 위상 정렬 수행
topology_sort(n, graph, indegree, result, time)