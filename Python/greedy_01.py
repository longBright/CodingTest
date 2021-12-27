# 2021.12.27 Greedy Algorithm Exercise
# 큰 수의 법칙 - p.92
# 배열의 크기 : N, 덧셈 횟수 : M, 가장 큰 수가 더해지는 횟수 : K -> 입력
# 출력 : 덧셈의 결과

# input N, M, K
n, m, k = map(int, input().split())

# 배열 입력
data = list(map(int, input().split()))

if len(data) != n :
    print('Error Occured! N 개의 정수를 입력하세요!')
    exit(0)

data.sort()

first = data[n-1]       # max value
second = data[n-2]      # second value

# result of this prob
result = 0

# Get result
while(True):
    for i in range(k):
        if m == 0: break
        result += first
        m -= 1
    if m == 0: break
    result += second
    m -= 1
print(result)