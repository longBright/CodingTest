# 22.05.14 1931번
# 회의실 배정

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = data[0][1]
for i in range(1, n):
    if data[i][0] >= end:
        cnt += 1
        end = data[i][1]
print(cnt)
