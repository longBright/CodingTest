# 2021.01.04 Implementation Exercise
# 예제 4-2 시각 - p.113

# 정수 입력
N = int(input())

cnt = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                cnt += 1
                
print(cnt)