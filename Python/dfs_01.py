# solution
def solution(x, y, g):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    else:
        # 미방문 노드일 경우
        if g[x][y] == 0:
            g[x][y] = 1     # 방문처리
            # 상하좌우 방문
            solution(x-1, y, g)
            solution(x+1, y, g)
            solution(x, y-1, g)
            solution(x, y+1, g)
            return True         # 조건만족, 0의 영역 +1
        # 방문 노드인 경우 조건 불만족.
        return False

# N, M 입력
n, m = map(int, input().split())

# 그래프 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# DFS 실행
ans = 0
for i in range(n):
    for j in range(m):
        if solution(i, j, graph):
            ans += 1
            
print(ans)