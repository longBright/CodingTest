# 22.05.12 11508번
# 2+1 세일

n = int(input())

cost = []
for i in range(n):
    cost.append(int(input()))
cost.sort(reverse=True)

total = 0
for i in range(n):
    if(i % 3 != 2):
        total += cost[i]
print(total)


# cnt = 1
# total = 0
# for i in range(n):
#     if cnt == 3:
#         total += sum(cost[i-2:i])     # 마지막 원소인 i가 최솟값일 것이므로
#         cnt = 0     # 갯수 초기화
#     cnt += 1
#
# if len(cost) % 3 != 0:
#     total += cost[i]
# print(total)
