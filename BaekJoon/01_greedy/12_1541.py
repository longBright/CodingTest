# 22.05.14 1541번
# 잃어버린 괄호

data = input().split('-')
num = []
for i in data:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

# data = list(input().split('-'))
# print(data)
#
# for i in data:
#     if '+' in i:
#         s = i.split('+')
#         for j in s:
#             data.append(j)
#         data.remove(i)
#
# result = int(data[0])
# for i in range(1, len(data)):
#     result -= int(data[i])
# print(result)
