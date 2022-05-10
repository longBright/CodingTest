# 22.04.18 정렬 문제 구현
# 국영수

# 입력
n = int(input())

students = []
for i in range(n):
    students.append(input().split())

# sorted 함수 사용
result = sorted(students, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for res in result:
    print(res[0])
    