# 22.02.23 구현문제
# 자물쇠와 열쇠
# 아예 못 풀었음
# 놓친 아이디어 : 자물쇠 크기 확장

# 본 풀이는 열쇠의 크기가 3인 경우를 기준으로 작성되어있으므로, 3으로 작성된 부분을 len(key) 로 하는 것이 더 매끄러울것으로 예상


# 2차원 리스트 90도 회전
def rotate_matrix_by_90_degree(a):
    row_length = len(a)
    col_length = len(a[0])
    
    res = [[0] * row_length for _ in range(col_length)]
    
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = a[r][c]
    return res

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

# solution 함수
def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # 자물쇠의 크기를 기존의 3배로 확장
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock):
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False