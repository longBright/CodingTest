# 재귀함수로 별 찍기
# N : 3의 거듭제곱이라고 할 때, 크기 N의 패턴은 N x N 정사각형 모양
# if N > 3 -> 공백으로 채워진 가운데의 N / 3 * N /3 정사각형을 크기 N/3 의 패턴으로 둘러쌈
# N은 3의 거듭제곱. N = 3^k

n = int(input())

def print_star(n):
    for i in range(n):
        for j in range(n-1):
            if (j % 3 == 1 and i % 3 == 1):
                print(' ', end='')
            else:
                print('*', end='')
        print('*')

for i in range(n):
    if i % 3 == 1:
        print_star(n)