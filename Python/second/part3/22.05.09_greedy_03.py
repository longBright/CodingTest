# 22.05.09 그리디 기출 문제
# 문자열 뒤집기
# 첫번째 if 까지는 접근 잘 했음. 두번째 if 에서 좀 버벅거렸음

s = input()

cnt1 = 0    # 1 로 시작한 경우
cnt0 = 0    # 0 으로 시작한 경우
# 기본 값 : 1
if s[0] == 1:
    cnt1 += 1
else:
    cnt0 += 1

n = len(s)
for i in range(n-1):
    # 다음 숫자가 다른 숫자일 경우 cnt 값 증가
    if s[i] != s[i+1]:
        if s[i+1] == 1:     # 다음 수가 1인 경우
            cnt0 += 1
        else:               # 다음 수가 0인 경우
            cnt1 += 1
print(min(cnt0, cnt1))
