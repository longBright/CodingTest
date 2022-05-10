# 22.04.18 정렬 문제
# 실패율

def solution(n, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, n+1):
        cnt = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
        
        answer.append((i, fail))
        length -= cnt
    answer = sorted(answer, key=lambda ans:(ans[1]), reverse=True)
    return answer

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

answer = solution(n, stages)
print(answer)