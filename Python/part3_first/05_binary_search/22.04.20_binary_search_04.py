# 22.04.20 이진탐색 문제
# 가사 검색

from bisect import bisect_left, bisect_right

SIZE = 10001


def count_by_range(data, l_val, r_val):
    l_idx = bisect_left(data, l_val)
    r_idx = bisect_right(data, r_val)

    return r_idx - l_idx


def solution(words, queries):
    arr = [[] for _ in range(SIZE)]
    reversed_arr = [[] for _ in range(SIZE)]
    result = []

    # 길이별 단어 리스트 생성
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    # 이진 탐색을 위한 정렬
    for i in range(SIZE):
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:
        # 접미사에 와일드 카드가 붙은 경우
        if q[0] != '?':
            result.append(count_by_range(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z')))
        # 접두사에 와일드 카드가 붙은 경우
        else:
            result.append(count_by_range(reversed_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z')))
    return result


words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

answer = solution(words, queries)
print(answer)