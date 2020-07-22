import sys

input = sys.stdin.readline
n, h = map(int, input().split())
huddle = [0] * h

for i in range(n // 2):
    huddle[int(input())] -= 1
    huddle[h - int(input())] += 1

minn, num = n // 2, 0
hud = n // 2

for i in huddle:
    hud += i
    if hud < minn:
        minn = hud
        num = 1
    elif hud == minn:
        num += 1

print(minn, num)

