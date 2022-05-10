# 22.05.09 그리디 기출문제
# 곱하기 혹은 더하기

s = input()
n = len(s)

result = 0
for i in range(n):
    result = max(result + int(s[i]), result * int(s[i]))
print(result)
