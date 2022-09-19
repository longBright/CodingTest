# 22.05.16 21314번
# 민겸수
# 틀렸음

s = input()

maxVal = ""
minVal = ""
N = 0
for i in range(len(s)):
    if s[i] == "M":
        N += 1
    elif s[i] == "K":   # K 일 때
        if N > 0:       # M 을 만났을 때
            maxVal += str(5 * (10 ** N))
            minVal += str((10 ** N) + 5)
        else:
            maxVal += "5"
            minVal += "5"
        N = 0

if N > 0:
    maxVal += '1' * N
    minVal += str(10 ** (N-1))

print(maxVal)
print(minVal)
