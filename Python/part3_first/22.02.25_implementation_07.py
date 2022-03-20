# 22.02.25 구현문제
# 치킨 배달

# 틀림
# 조합 라이브러리 몰라서 틀림
from itertools import combinations


def get_distance(house, chickens, distances):
    r1, c1 = house
    distance = int(1e9)
    for chicken in chickens:
        r2, c2 = chicken
        distance = min(distance, abs(r1-r2) + abs(c1-c2))
    distances.append(distance)
    
    
n, m = map(int, input().split())

city = []
for i in range(n):
    data = list(map(int, input().split()))
    city.append(data)

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:     # 집인 경우
            houses.append((i, j))
        elif city[i][j] == 2:   # 치킨 집인 경우
            chickens.append((i, j))

distances = []
for house in houses:
    get_distance(house, chickens, distances)
        
distances.sort()
result = 0
for i in range(m):
    result += distances[i]

print(distances)
print(result)