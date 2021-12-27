# 2021.12.27 Greedy Algorithm Exercise
# 1이 될 때까지 - p.99
# N 이 1이 될 때까지 아래 두 과정 중 하나를 반복적으로 선택하여 수행
# N >= K
# 1) N 에서 1 을 뺀다
# 2) N 을 K 로 나눈다 - N이 K로 나누어떨어질 때만 선택 가능
# 출력 : 총 연산 횟수

# N, K 입력
n, k = map(int, input().split())

cnt = 0
while(n >= k):
    # N 이 K 로 나누어 떨어지지 않으면
    while(n % k != 0):
        n -= 1
        cnt += 1
        print('n-=1')
    # N 이 K 로 나누어 떨어지면
    n //= k
    cnt += 1
    print('n//=k')

# N 이 1이 될 때까지 (최종 나눗셈 이후 N 이 1이 아닐 경우를 대비한다.)
while(n > 1):
    n -= 1
    cnt += 1
    print('n-=1')

print(cnt)