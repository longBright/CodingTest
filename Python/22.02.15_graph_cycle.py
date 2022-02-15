# 22.02.15 그래프 이론 - 서로소 집합을 활용한 사이클 판별

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)      # a의 루트
    b = find_parent(parent, b)      # b의 루트
    # a 의 루트가 b 의 루트보다 작으면 -> b의 루트 : a
    # b 의 루트가 a 의 루트보다 작으면 -> a의 루트 : b
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    # 루트 노드가 같으면 사이클 발생
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
        
if cycle:
    print('사이클 발생')
else:
    print('사이클 미 발생')