# 22.05.11 1343번
# 폴리오미노
# https://www.acmicpc.net/problem/1343

s = input()
s = s.replace('XXXX', 'AAAA')
s = s.replace('XX', 'BB')

if 'X' in s:
    print(-1)
else:
    print(s)
