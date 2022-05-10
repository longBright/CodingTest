# 22.05.06 그래프 이론 문제
# 행성 터널
# Kruskal Algorithm 적용. MST 문제
# 교재 풀이와 다른점 : 행성 정보 입력과 간선 처리에 대한 부분이 다름
# 교재 풀이의 시간 복잡도가 더 나아보임

# find 연산
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# union 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력 및 parent 테이블 초기화
n = int(input())
parent = [0] * (n+1)
for i in range(n):
    parent[i] = i

# 행성 좌표 입력
planets = []
for _ in range(n):
    planets.append(list(map(int, input().split())))
# 간선 정보 초기화
edges = []
for i in range(n):
    for j in range(i+1, n):
        cost_x = abs(planets[i][0] - planets[j][0])
        cost_y = abs(planets[i][1] - planets[j][1])
        cost_z = abs(planets[i][2] - planets[j][2])
        cost = min(cost_x, cost_y, cost_z)
        if (cost, i, j) not in edges:
            edges.append((cost, i, j))

edges.sort()
# Kruskal Algorithm
res = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
print(res)
