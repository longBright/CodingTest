# 22.05.05 그래프 이론 문제
# 여행 계획
# 서로소 집합 알고리즘 적용

# find 연산 함수
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
print(parent)

# 도시 연결 정보 입력
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        union_parent(parent, i, j)
plan = list(map(int, input().split()))

print(parent)
# 여행 가능 여부 확인
result = True
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print('YES')
else:
    print('NO')
