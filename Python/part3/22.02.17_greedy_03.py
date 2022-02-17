# 22.02.17 Part 3 그리디 문제
# 문자열 뒤집기

s = input()

first = s[0]
result = 0
for i in range(len(s)):
    if s[i] != first and s[i] != s[i-1]:
        result += 1
print(result)