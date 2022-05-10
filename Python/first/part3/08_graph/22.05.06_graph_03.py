# 22.05.06 그래프 이론 문제
# 어두운 길
# Kruskal Algorithm 적용. MST 문제

# find 연산
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# union 연산
def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# n, m 입력 및 parent 테이블 초기화
n, m = map(int, input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i

# 도시 정보(x,y,z) 입력
edges = []
for _ in range(m):
    x, y, z = map(int, input().split())     # x 에서 y 까지의 비용이 z
    edges.append((z, x, y))
edges.sort()    # 비용 기준 정렬

# Kruskal Algorithm
min_cost = 0
total_cost = 0
for edge in edges:
    cost, x, y = edge
    total_cost += cost
    # 사이클이 발생하지 않으면 MST 에 추가
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        min_cost += cost

# 절약 가능한 최대 금액 이므로 (전체 - 최소)
answer = total_cost - min_cost
print(answer)
