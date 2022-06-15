# 22.06.15 구현문제
# 문자열 압축

# 접근은 맞았는데 result 문자열 처리를 제대로 하지 못했음.

s = input()

answer = int(1000)
for i in range(1, len(s) // 2+1):
    temp = s[:i]
    cnt = 1
    result = ""
    for j in range(i, len(s), i):
        if temp == s[j:j+i]:
            cnt += 1
        else:
            # result += str(cnt) + temp 으로 했었음.
            result += str(cnt) + temp if cnt >= 2 else temp
            temp = s[j:j+i]
            cnt = 1
    # 남아있는 문자열에 대한 처리
    result += str(cnt) + temp if cnt >= 2 else temp
    print(result)
    answer = min(answer, len(result))
print(answer)
