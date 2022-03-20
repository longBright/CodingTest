# 22.03.17 DFS/BFS 문제
# 괄호 변환
# 답 보고 풀었음

# 입력
p = input()

def solution(p):
    if len(p) == 0:
        return p
    
# 올바른 문자열 여부 확인
def is_right(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

# 균형잡힌 문자열 인덱스 확인
def bal_idx(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i
        
def sol(p):
    answer = ''
    if p == '':
        return answer
    idx = bal_idx(p)
    u = p[:idx+1]
    v = p[idx+1]
    # 올바른 문자열이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if is_right(u):
        answer = u + sol(v)
    # 올바른 문자열이 아니면
    else:
        answer = '('
        answer += sol(v)
        answer += ')'
        u = list(u[1:-1])   # 맨 앞, 맨 뒤 문자 제거
        # 좌,우 괄호 방향 전환
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)    # 뒤에 괄호 방향이 바뀐 문자열 뒤에 붙임
    return answer