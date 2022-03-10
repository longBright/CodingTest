# 22.02.17 Part 3 그리디 문제
# 무지의 먹방 라이브
# 틀림 그냥 틀려버림

def solution(food_times, k):
    answer = 0
    last = len(food_times) - 1
    for i in range(k):
        if food_times[answer] == 0:
            answer += 1
            if answer == last:
                answer = 0
                food_times[answer] -= 1
    answer += 1
    if answer == last:
        answer = 0
        if food_times[answer] == 0:
            answer = -1
    return answer

food_times = list(map(int, input().split()))
k = int(input())

answer = solution(food_times, k)
print(answer)