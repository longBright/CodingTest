# 22.04.29 DP 문제
# 편집 거리

str1 = input()
str2 = input()
n = len(str1)
m = len(str2)

# 공 문자열을 dp 테이블에 추가하므로 +1
dp = [[0] * (m+1) for _ in range(n+1)]    # 원본 문자열 길이 -> 행 개수, 타겟 문자열 길이 -> 열 개수

# 첫번째 행과 첫번째 열 초기화
# dp[0][0] 은 어차피 0 이므로 제외하고 초기화하도록 함. 같이 초기화해도 결과는 상관 없긴함
for i in range(1, n+1):
    dp[i][0] = i
for i in range(1, m+1):
    dp[0][i] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        # 두 문자열이 같을 경우
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 두 문자열이 다를 경우, 1 + min(insert, remove, replace)
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
print(dp[n][m])

# dp 테이블 결과 확인
for d in dp:
    print(d)