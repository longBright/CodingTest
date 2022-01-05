# 피보나치 수
# 0번째 피보나치 : 0 1번째 피보나치 : 1 그 이후로는 앞 두 수의 합
# Fn = Fn-1 + Fn-2 (n>=2)
# 입력 : n, 출력 : n번째 피보나치 수

n = int(input())

def Fib(n):
    if (n < 0):
        return -1
    elif (n <= 1):
        return n
    else:
        return (Fib(n-1) + Fib(n-2))
    
answer = Fib(n)
print(answer)