# 22.02.17 Part 3 그리디 문제
# 문자열 뒤집기

s = input()

first = s[0]    # 첫번째 숫자 선정
result = 0
for i in range(len(s)):
    if s[i] != first and s[i] != s[i-1]:        # 첫번째 숫자와 다르고 이전 숫자와 다르면
        result += 1                             # 뒤집기 횟수 증가
print(result)