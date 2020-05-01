import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
wall = [list(input()) for _ in range(n)]
dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1:
            return dist[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny][w]:
                continue
            if wall[nx][ny] == '0':
                dist[nx][ny][w] = dist[x][y][w] + 1
                q.append((nx, ny, w))
            if wall[nx][ny] == '1' and w == 0:
                dist[nx][ny][1] = dist[x][y][w] + 1
                q.append((nx, ny, 1))
    return -1
print(bfs)


