# 22.05.07 그래프 이론 문제
# 최종 순위
# 위상 정렬 적용
# 틀렸음.

from collections import deque


# 위상정렬 함수(원본에서 수정 필요함)
def topology_sort(graph, indegree, n):
    result = []
    possible = True
    q = deque()
    # 차수가 0인 노드부터 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 있는 동안
    while q:
        now = q.popleft()
        result.append(now)
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if graph[i][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
    return possible, result


# 팀의 수 입력
n = int(input())

# 그래프 초기화
graph = [[False] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i+1, n+1):
        graph[i][j] = True

# 차수 테이블 초기화
indegree = [0] * (n+1)
data = list(map(int, input().split()))
for x in data:
    indegree[x] = x - 1

# 상대적인 등수가 바뀐 쌍의 수 입력
m = int(input())
# 입력된 쌍의 차수 변경
for _ in range(m):
    a, b = map(int, input().split())
    indegree[a] += 1
    indegree[b] -= 1

# 위상정렬 수행
possible = False
possible, result = topology_sort(graph, indegree, n)

if possible:
    for x in result:
        print(x, end=' ')
else:
    print("IMPOSSIBLE")
