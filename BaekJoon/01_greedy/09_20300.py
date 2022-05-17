# 22.05.13 20300번
# 서강근육맨

n = int(input())
t = list(map(int, input().split()))
t.sort()

# 운동기구 개수가 홀수이면 최댓값을 리스트에서 제거
# 짝수개이면 최댓값 따로 저장
if len(t) % 2 != 0:
    m = t.pop()
else:
    m = t[n-1]

# 
for i in range(len(t)):
    m = max(m, t[i] + t[len(t) - i - 1])
print(m)
