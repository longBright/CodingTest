# 22.02.05 그리디 알고리즘 연습문제
# 1이 될 때까지

# input
n, k = map(int, input().split())

result = 0
while(True):
    if n == 1:
        break
    else:
        if n % k == 0:
            n /= k
            result += 1
        else:
            n -=1
            result += 1
            
print(result)