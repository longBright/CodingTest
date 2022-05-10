# 22.04.28 DP 문제
# 병사 배치하기
# 가장 긴 증가하는 부분 수열 문제 : 하나의 수열이 주어졌을 때, 값들이 증가하는 형태의 가장 긴 수열을 찾는 문제
# 위 문제의 점화식 : all 0<= j < i, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
# 아래는 예제에 대한 구현
# n = 5
# array = [10, 20, 10, 30, 50,]
#
# dp = [1] * n
# for i in range(n):
#     for j in range(i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(dp)
# print(max(dp))

# 문제 구현(교재 답안)
n = int(input())
array = list(map(int, input().split()))
array.reverse()
print(array)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
result = n - max(dp)
print(result)


# 문제 구현(내가 푼 방식)
array.reverse()
print(array)
d = [1] * n
for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))
