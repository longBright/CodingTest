# 22.05.12 13305번
# 주유소
# https://www.acmicpc.net/problem/13305
# 틀림

# 1. 도시의 기름값 배열을 탐색하며 현재 최저값보다 더 작은 값이 나오면 갱신하면서 풀어가면 된다.
# 2. 첫 도시의 기름값을 minVal로 두고 roads를 탐색하며 같은 위치 도시의 기름값이 더 작으면 그 값으로 minVal을 바꾸고, 도로 길이를 곱한 값을  total에 더한다.

N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]      # 첫 도시의 기름값을 minVal 로 설정
total = 0
for i in range(N - 1):  # 도로 개수 : N-1 개
    if minVal > cities[i]:  # 같은 위치 도시의 기름값이 더 적으면 minVal 교체.
        minVal = cities[i]
    total += (minVal * roads[i])    # 도로 길이를 곱한 값을 더함
    print(total)
print(total)
