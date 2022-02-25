# 22.02.24 구현 문제
# 기둥과 보 설치

# 틀림
# check 메소드 구현을 틀렸음
# for 루프 내에서 모든 구조물들에 대한 점검을 진행해야함

# 명령 수행 가능 여부 체크
def check(n, x, y, a, answer):
    # 범위 초과
    if x < 0 or x > n or y < 0 or y > n:
        return False
    else:
        # 기둥
        if a == 0: 
            if y == 0:      # 바닥
                return True
            elif [x-1, y, 1] in answer or [x, y, 1] in answer:
                return True
            elif [x, y-1, 0] in answer:
                return True
            else:
                return False
        # 보
        elif a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                return True
            elif [x-1, y, 1] in answer or [x+1, y, 1] in answer:
                return True
            else:
                return False
        return True
def solution(n, build_frame):
    answer = []
    for data in build_frame:
        x, y, a, b = data
        # 명령 수행 여부 확인
        if check(n, x, y, a, answer):
            if b == 0:
                if [x, y, a] in answer:
                    answer.remove([x,y,a])
                    if check(n, x, y, a, answer):
                        answer.append([x,y,a])
            else:
                if [x, y, a] not in answer:
                    answer.append([x,y,a])
                
    return sorted(answer)
            
# n = int(input())
# r, c = map(int, input().split())

n = 5
build_frame = [[1,0,0,1],
               [1,1,1,1],
               [2,1,0,1],
               [2,2,1,1],
               [5,0,0,1],
               [5,1,0,1],
               [4,2,1,1],
               [3,2,1,1]]

build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

# for i in range(r):
#     x,y,a,b = map(int, input().split())
#     build_frame[i] = list(x,y,a,b)
     
result = solution(n, build_frame)
print(result)