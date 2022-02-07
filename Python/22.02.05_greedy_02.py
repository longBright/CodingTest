# 22.02.05 그리디 알고리즘 연습문제
# 숫자 카드 게임

# input
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
print(arr)

min_list = []
for i in range(n):
    min_list.append(min(arr[i]))

result = max(min_list)
print(result)