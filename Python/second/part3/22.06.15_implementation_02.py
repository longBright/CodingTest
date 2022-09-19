# 22.06.15 구현문제
# 문자열 재정렬
s = input()

result = []
total = 0
for c in s:
    if c.isalpha():
        result.append(c)
    else:
        total += int(c)
result.sort()

for x in result:
    print(x, end="")
print(total)
