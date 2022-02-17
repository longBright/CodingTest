# 22.02.17 그래프 이론 문제
# 도시 분할 계획

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 둘 중 값이 작은 노드가 부모 노드가 됨
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    
# 노드, 간선 개수 입력
n, m = map(int, input().split())
parent = [0] * (n+1)

# 루트 테이블 초기화
for i in range(1, n+1):
    parent[i] = i

# 간선 정보 입력
edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()        # 비용 기준 정렬

# 크루스칼 알고리즘 수행
result = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않으면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)      # MST 에 추가
        result += cost                  # MST 총 비용에 추가
        last = cost
result -= last     # 마지막 간선 비용 제거(두 개의 MST 생성)
print(result)
