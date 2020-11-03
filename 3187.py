from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j):
    global v, k, tv, tk
    visit[i][j] = 1
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and s[nx][ny] != "#":
                q.append([nx, ny])
                visit[nx][ny] = 1
                if s[nx][ny] == "v": tv += 1
                if s[nx][ny] == "k": tk += 1
    if tv > 0 and tk > 0:
        if tv >= tk: k -= tk
        else: v -= tv
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())
v, k = 0, 0
va, ka = [], []
s = []
for i in range(r):
    a = list(input().strip())
    s.append(a)
    for j in range(c):
        if a[j] == "v": v += 1
        if a[j] == "k": k += 1
visit = [[0] * c for i in range(r)]
for i in range(r):
    for j in range(c):
        if visit[i][j] == 0 and s[i][j] != "#":
            tv, tk = 0, 0
            if s[i][j] == "v": tv += 1
            elif s[i][j] == "k": tk += 1
            bfs(i, j)
print(k, v)