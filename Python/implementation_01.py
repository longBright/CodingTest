# 2021.12.29 Implementation Exercise
# 상하좌우 - p.110

# N, 여행계획(plan) 입력
n = int(input())
plans = input().split()

# 시작 위치 : 1행 1열
loc = [1, 1]

for plan in plans:
    if loc[1] > 1 and plan == 'L':
        loc[1] -= 1
    if loc[1] < n and plan == 'R':
        loc[1] += 1
    if loc[0] > 1 and plan == 'U':
        loc[0] -= 1
    if loc[0] < n and plan == 'D': 
        loc[0] += 1
        
# 도착 위치 : loc[0] 행 loc[1] 열
print(loc[0], loc[1])