# 22.02.17 Part 3 그리디 문제
# 곱하기 혹은 더하기

# 문자열 입력
s = input()

result = 0
for i in s:
    i = int(i)
    if i == 0:
        continue
    else:
        result = max(result + i, result * i)
print(result)