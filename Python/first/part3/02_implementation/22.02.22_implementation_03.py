# 22.02.22 구현 문제
# 문자열 압축

# 못풀었음
# 반복문의 조건까지는 접근했음
# 내부 if 문들 접근에 실패했음

def sol(s):
    answer = len(s)
    n = len(s) // 2
    
    compressed = ""     # 압축된 문자열
    # 1부터 n+1까지
    for i in range(1, n + 1):
        prev = s[0:i]       # i개 단위로 자를 첫 문자
        cnt = 1
        # i 개 단위로 잘라서 진행
        for j in range(i, len(s), i):
            # 두 문자열이 같은 경우
            if s[j:j+i] == prev:
                cnt += 1
            # 두 문자열이 다른 경우
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev     # 문자열에 양식에 맞춰서 추가
                # 값 초기화
                cnt = 1
                prev = s[j:j+i]
        # 뒷부분 문자열 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compressed))
        print(f'{i} 개 단위로 자를 경우 문자열 : {compressed}')
    return answer

s = input()

answer = sol(s)
print(answer)