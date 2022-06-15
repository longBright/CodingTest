# 22.06.15 구현문제
# 럭키 스트레이트
n = input()
center = len(n) // 2
left = n[:center]
right = n[center:]

l_sum = 0
r_sum = 0
for num in left:
    l_sum += int(num)
for num in right:
    r_sum += int(num)

if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")
