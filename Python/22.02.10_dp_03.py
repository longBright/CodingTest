# 22.02.10 다이나믹 프로그래밍
# 바닥 공사

# 이거도 못풀었음

# 재귀함수로 구현
def sol(x):
    if x <= 1:
        return x
    elif x == 2:
        return 3
    else:
        return sol(x-1) + sol(x-2) * 2

# input
n = int(input())


# dp 테이블
d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]*2
print(d[n]  % 796796)


result = sol(n) % 796796
print(result)