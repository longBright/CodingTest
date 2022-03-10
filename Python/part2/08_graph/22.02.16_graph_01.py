# 22.02.16 그래프 이론 문제
# 팀 결성

# 루트 노드 반환 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
n, m = map(int, input().split())
# 루트 테이블 초기화
parent = [0] * (n+1)
# 루트 테이블 - 자기 자신으로 초기화
for i in range(n+1):
    parent[i] = i
    
for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")