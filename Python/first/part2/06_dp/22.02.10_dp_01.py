# 22.02.10 다이나믹 프로그래밍
# 1로 만들기

def sol(d, x):
    if x % 5 == 0:
        d[x] = min(d[x-1] + 1, d[x//5] + 1)
    elif x % 3 == 0:
        d[x] = min(d[x-1] + 1, d[x//3] + 1)
    elif x % 2 == 0:
        d[x] = min(d[x-1] + 1, d[x//2] + 1)
    else:
        d[x] = d[x-1] + 1

# input
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    sol(d, i)
print(d[x])