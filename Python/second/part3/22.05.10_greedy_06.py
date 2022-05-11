# 22.05.10 그리디 기출 문제
# 무지의 먹방 라이브
# 틀림. 정확성 : 32.1 / 효율성 : 0.0 => 본 문제는 교재의 답안대로 속도가 더 빠른 우선순위 큐를 사용해야함
# 내가 작성한 코드는 주석 처리로 폐기(하단에 있음)

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1 리턴
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 사용
    q = []
    n = len(food_times)     # 남은 음식의 개수
    for i in range(n):
        # (음식시간, 음식번호) 형태로 우선순위 큐 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_val = 0     # 먹기 위해 사용한 시간
    prev = 0        # 직전에 다 먹은 음식 시간

    # sum_val + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_val + ((q[0][0] - prev) * n) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now - prev) * n
        n -= 1  # 다 먹은 음식 제외
        prev = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    answer = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return answer[(k - sum_val) % n][1]


print(solution([3, 1, 2], 5))


# def solution(food_times, k):
#     n = len(food_times) - 1
#     now = 0
#     # k 초 동안 반복
#     for _ in range(k):
#         food_times[now] -= 1        # 음식 섭취
#         now = move_to_next(now, n)  # 다음 음식으로 이동
#         # 식사 시간이 남은 음식 탐색
#         for i in range(n):
#             if food_times[now] == 0:
#                 now = move_to_next(now, n)
#             elif sum(food_times) <= 0:
#                 return -1
#     return move_to_next(now, n)
#
#
# # 다음 음식으로 이동
# def move_to_next(now, n):
#     if now == n:    # 마지막 인덱스인 경우
#         now = 0
#     else:           # 마지막 인덱스가 아닌 경우
#         now += 1
#     return now
