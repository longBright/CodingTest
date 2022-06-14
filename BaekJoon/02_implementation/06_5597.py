# 22.06.14 5579번
# 과제 안 내신 분

data = []
for _ in range(28):
    data.append(int(input()))

result = []
for i in range(1, 31):
    if i not in data:
        result.append(i)
print(min(result))
print(max(result))