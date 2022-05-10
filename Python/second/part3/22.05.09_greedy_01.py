# 22.05.09 그리디 기출문제
# 모험가 길드

n = int(input())
data = list(map(int, input().split()))

# 내 풀이
data.sort(reverse=True)
result = 0
for x in data:
    if n >= x:          # 포함할 모험가 수가 공포도 이상일 경우
        n -= x
        result += 1     # 그룹 수 증가
    elif n < x:         # 포함할 모험가 수가 공포도 미만일 경우
        break           # 루프 종료
print(result)

# 책 풀이
data.sort()
cnt = 0
res = 0
for x in data:
    cnt += 1
    if cnt >= x:
        res += 1
        cnt = 0
print(res)