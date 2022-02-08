# 22.02.08 정렬 문제
# 두 배열의 원소 교체

# input
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
    
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

result = sum(a)
print(result)