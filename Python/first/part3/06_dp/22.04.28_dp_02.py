# 22.04.28 DP 문제
# 정수 삼각형

# input
n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):       # 1번부터 진행(0번은 연산 불가능)
    for j in range(i+1):    # 삼각형 이므로 i번 리스트의 i+1 개가 원소의 개수
        # 바로 위
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        # 대각선 왼쪽
        if j == 0:
            left = 0
        else:
            left = dp[i-1][j-1]
        dp[i][j] = dp[i][j] + max(up, left)     # 점화식에 의한 최댓값 저장

result = max(dp[n-1])
print(result)
