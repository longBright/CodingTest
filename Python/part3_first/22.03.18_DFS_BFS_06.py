# 22.03.18 DFS/BFS 문제
# 감시 피하기
# 틀렸음
# 교재 예시 답안과 다른 방식으로 구현했음
# 교재 예시 답안 방식 : 06(2)

# 입력
n = int(input())

# 그래프 입력
graph = []
temp = []
result = False
for i in range(n):
    graph.append(list(input().split()))
    
# 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 감시 메소드. 학생을 찾으면 True, 못찾으면 False 반환
def monitor(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if temp[nx][ny] == 'S':
                print('yes')
                return True
            elif temp[nx][ny] == 'O':
                return False
            else:
                monitor(nx, ny)
    return False


def sol(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    result = monitor(i, j)
                    if result == True:
                        return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    cnt += 1
                    sol(cnt)
                    graph = 'X'
                    cnt -= 1
                    
if result:
    print('NO')
else:
    print('YES')