# 22.05.13 20115번
# 에너지 드링크

N = int(input())
X = list(map(int, input().split()))
X.sort()

result = X[-1]
for i in range(N-1):
    result += X[i] / 2
print(result)

# 시간 초과 답안
# max() 함수를 쓸 필요가 없음. 어차피 maxVal + minVal/2 가 사용됨.
# while X:
#     if len(X) == 1:
#         break
#     a = min(X)
#     b = max(X)
#     X.remove(a)
#     X.remove(b)
#     nx = max(a + b/2, b + a/2)
#     X.append(nx)
# print(X[0])
