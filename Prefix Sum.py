n = int(input())
data = list(map(int, input().split()))

# Prefix Sum 배열 계산
Sum = 0
PrefixSum=[0]
for i in data:
    Sum += i
    PrefixSum.append(Sum)

print(PrefixSum)
# 구간 합 계산

left = 4
right = 5
print(PrefixSum[right] - PrefixSum[left-1])
