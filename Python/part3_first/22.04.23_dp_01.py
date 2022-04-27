# 22.04.23 다이나믹 프로그래밍 문제
# 금광
# 접근을 잘못함. 점화식을 통한 구현이 아니라 구현문제처럼 접근했음
# 아무튼 틀림

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(data[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] += max(left, left_up, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)