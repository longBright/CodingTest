# 22.02.17 Part 3 그리디 문제
# 모험가 길드
# 답봤음

# 모험가 수 입력
n = int(input())

# 모험가 별 공포도 입력
data = list(map(int, input().split()))
data.sort()

cnt = 0
result = 0
for x in data:
    cnt += 1
    if cnt >= x:
        cnt = 0
        result += 1
print(result)