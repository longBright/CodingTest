# 22.05.28 2812번
# 크게 만들기
# 접근부터 틀림

n, k = map(int, input().split())
num = input()
ans = []
del_cnt = k
for i in range(n):
    while len(ans) > 0 and del_cnt > 0:
        if int(ans[-1]) < int(num[i]):
            ans.pop()
            del_cnt -= 1
        else:
            break
    ans.append(num[i])

ans = ''.join(ans)
print(ans[:n-k])