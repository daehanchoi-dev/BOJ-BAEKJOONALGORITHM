import sys
import collections

wheels = []
turns = []


def turnLeft(i, d):
    if i < 0:
        return

    if wheels[i][2] != wheels[i + 1][6]:
        turnLeft(i - 1, -d)
        wheels[i].rotate(d)


def turnRight(i, d):
    if i > 3:
        return

    if wheels[i][6] != wheels[i - 1][2]:
        turnRight(i + 1, -d)
        wheels[i].rotate(d)


def solve():
    for turn in turns:
        [idx, direction] = turn

        turnLeft(idx - 1, -direction)
        turnRight(idx + 1, -direction)

        wheels[idx].rotate(direction)


if __name__ == '__main__':
    for i in range(4):
        wheels.append(collections.deque(list(sys.stdin.readline())[:8]))

    K = int(sys.stdin.readline())

    for i in range(K):
        v1, v2 = map(int, sys.stdin.readline().split())
        turns.append([v1 - 1, v2])

    solve()
    sumVal = 0
    for i, wheel in enumerate(wheels):
        sumVal += int(wheel[0]) * (1 << i)
    print(sumVal)