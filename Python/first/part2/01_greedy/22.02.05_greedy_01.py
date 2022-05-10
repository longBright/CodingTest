# 22.02.05 그리디 알고리즘 연습문제
# 큰 수의 법칙

# input
n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

cnt = 0
result = 0
for i in range(m):
    if cnt != k:
        cnt += 1
        result += arr[n-1]
    else:
        cnt = 0
        result += arr[n-2]
        
print(result)

#==================================================#
# 예시 답안 1
temp = m    # 예시답안 2를 위해 m 백업
result = 0
while(True):
    for i in range(k):
        if m == 0:
            break
        result += arr[n-1]
        m -= 1
    if m == 0:
        break
    result += arr[n-2]
    m -= 1
    
print(result)
#===================================================#

m = temp    # 예시 답안 1에서 m을 0으로 만들기 때문에 백업데이터 복구
# 예시 답안 2
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * arr[n-1]
result += (m - count) * arr[n-2]

print(result)