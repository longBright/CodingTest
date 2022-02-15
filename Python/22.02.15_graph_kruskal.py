# 22.02.15 그래프 이론 - 크루스칼 알고리즘

from re import L


def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def uninon_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)
# 루트 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력
edges = []
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

result = 0
for edge in range(edges):
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        uninon_parent(parent, a, b)
        result += cost
print(result)