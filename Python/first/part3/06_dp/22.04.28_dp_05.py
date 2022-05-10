# 22.04.28 DP 문제
# 못생긴 수
# 못생긴 수 : 2,3,5 만을 약수로 가지는 수.(1 포함으로 가정)
# 문제 접근을 못했음.

n = int(input())

ugly = [0] * n  # dp 테이블
ugly[0] = 1     # 첫번째 원소 초기화

idx2 = idx3 = idx5 = 0    # 2, 3, 5 의 배수가 들어갈 인덱스
next2, next3, next5 = 2, 3, 5   # 2, 3, 5 의 배수. 2,3,5로 초기화
# 0 번 인덱스 원소의 값은 이미 있으므로, 1 부터 시작
for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        idx2 += 1
        next2 = ugly[idx2] * 2
    if ugly[i] == next3:
        idx3 += 1
        next3 = ugly[idx3] * 3
    if ugly[i] == next5:
        idx5 += 1
        next5 = ugly[idx5] * 5
print(ugly[n-1])
