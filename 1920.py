import sys

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in range(N):
    if m[i] in n:
        print(1)
    else:
        print(0)

