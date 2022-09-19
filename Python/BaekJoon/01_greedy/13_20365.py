# 22.05.16 20365번
# 블로그

n = int(input())
s = input()

cntR = 0
cntB = 0

if s[0] == 'R':
    cntR += 1
else:
    cntB += 1

for i in range(n-1):
    if s[i] != s[i+1]:
        if s[i+1] == 'R':
            cntB += 1
        else:
            cntR += 1

print(max(cntB, cntR))
