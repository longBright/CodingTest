# 22.05.25 2812번
# 크게 만들기
# 다시

n, k = map(int, input().split())
string = input()

sorted_s = []
for i in range(n):
    sorted_s.append(int(string[i]))
sorted_s.sort()
print(sorted_s)

cnt = 1
result = ""
for i in range(n):
    if cnt == k:
        break
    if int(string[i]) <= sorted_s[k]:
        string = string.replace(string[i], "")
        cnt += 1
print(string)
