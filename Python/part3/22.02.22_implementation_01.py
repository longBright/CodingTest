# 22.02.22 구현 문제
# 럭키 스트레이트

def sol(str):
    result = 0
    for s in str:
        result += int(s)
    return result

n = input()

mid = len(n) // 2
left = n[0:mid]
right = n[mid:]

if sol(left) == sol(right):
    print("LUCKY")
else:
    print("READY")