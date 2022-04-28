# 22.04.18 정렬 문제
# 카드 정렬하기

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)

result = 0
while(len(data) > 1):
    a = data.pop()
    b = data.pop()
    result += a+b
    data.append(a+b)

print(result)