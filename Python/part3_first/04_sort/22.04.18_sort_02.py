# 22.04.18 정렬문제
# 안테나

# 입력
n = int(input())

houses = list(map(int, input().split()))
houses.sort()

result = houses[(n-1) // 2]
print(result)