# 22.02.08 정렬 문제
# 위에서 아래로
# 단순한 내림차순 출력문제

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))
    
arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')