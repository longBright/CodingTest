# 22.02.22 구현 문제
# 문자열 재정렬

def sol(s, array):
    sum = 0 
    for c in s:
        if ord(c) >= 65 and ord(c) <= 114:
            array.append(c)
        else:
            sum += (ord(c) - 48)
    array.sort()
    array.append(str(sum))
    return array
    
s = input()

array = []

sol(s, array)

for i in array:
    print(i,end='')