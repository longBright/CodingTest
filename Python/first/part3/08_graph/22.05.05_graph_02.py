# 22.05.05 그래프 이론 문제
# 탑승구
# 접근 못했음
# 서로소 집합 알고리즘을 적용해야함

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

G = int(input())
P = int(input())
parent = [0] * (G+1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(G+1):
    parent[i] = i

# union 연산 수행
res = 0
for _ in range(P):
    data = int(input())
    # 루트가 0 이면 종료
    if find_parent(parent, data) == 0:
        break
    # 루트가 0이 아니면 진행
    union_parent(parent, data, data-1)      # 바로 좌측의 집합과 union 연산 수행
    res += 1
print(res)