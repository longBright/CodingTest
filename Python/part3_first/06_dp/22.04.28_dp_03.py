# 22.04.28 DP 문제
# 퇴사
# 그냥 틀림 아예 못품

n = int(input())    # n
T = []              # 시간 리스트 T
P = []              # 보상 리스트 P
dp = [0] * (n+1)    # dp 테이블
max_value = 0       # 최댓값
# T, P 입력
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 뒤부터 진행
for i in range(n-1, -1, -1):
    t = T[i] + i
    # 기간 내 상담 종료
    if t <= n:
        dp[i] = max(P[i] + dp[t], max_value)
        max_value = dp[i]
    # 기간 초과
    else:
        dp[i] = max_value
print(max_value)
