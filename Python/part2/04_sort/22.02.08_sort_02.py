# 22.02.08 정렬 문제
# 성적이 낮은 순서로 학생 출력하기

# input
n = int(input())

arr = []
for i in range(n):
    temp = input().split()
    arr.append((temp[0], int(temp[1])))

arr.sort(key=lambda student: student[1])
for student in arr:
    print(student[0], end=' ')