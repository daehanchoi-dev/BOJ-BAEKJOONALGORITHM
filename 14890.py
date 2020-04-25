import sys
import itertools

N = L = 0
arr = []


def canGoPath(heights):
    current = heights[0]
    visited = [False for i in range(N)]

    for i, height in enumerate(heights):
        ## 높이가 똑같으면 그냥 진행
        if current == height:
            continue

        ## 높은 곳으로 이동
        ## 지금까지 이동한 거리가 L보다 크거나 같으면 이동가능
        elif current + 1 == height:
            for j in range(i - 1, i - 1 - L, -1):
                if j < 0 or current != heights[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = height

        ## 낮은 곳으로 이동
        ## 앞으로 이동할 곳에서 L만큼 같은 거리가 있으면 가능
        elif current - 1 == height:
            for j in range(i, i + L):
                if j >= N or current - 1 != heights[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = height

        ## 높이 차이가 1 이상이면 불가능
        else:
            return False

    return True


def solve():
    count = 0
    for i in range(N):
        if canGoPath(arr[i]):
            count += 1

    for j in range(N):
        path = []
        for i in range(N):
            path.append(arr[i][j])

        if canGoPath(path):
            count += 1

    print(count)


if __name__ == '__main__':
    N, L = map(int, sys.stdin.readline().split())

    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    solve()