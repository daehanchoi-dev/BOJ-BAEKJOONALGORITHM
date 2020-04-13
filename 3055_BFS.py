import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
mat = [[] for i in range(h)]
for i in range(h):
    ss = input().strip()
    for s in ss:
        mat[i].append(s)
q = deque()
for i in range(h):
    for j in range(w):
        if mat[i][j] == 'D':
            d_y = i
            d_x = j
        elif mat[i][j] == 'S':
            s_y = i
            s_x = j
        elif mat[i][j] == '*':
            q.append([i, j])
q.append([s_y, s_x])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    global q
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < w and 0 <= ny < h:
                if mat[ny][nx] == 'X':
                    continue
                elif mat[y][x] == '*':
                    if mat[ny][nx] == 'D':
                        continue
                    elif mat[ny][nx] == '.':
                        mat[ny][nx] = -1
                        q.append([ny, nx])
                elif mat[y][x] == 'S':
                    if mat[ny][nx] == 'D':
                        mat[ny][nx] = 1
                        return
                    elif mat[ny][nx] == '.':
                        mat[ny][nx] = 1
                        q.append([ny, nx])
                elif mat[y][x] < 0:
                    if mat[ny][nx] == 'D':
                        continue
                    elif mat[ny][nx] == '.':
                        mat[ny][nx] = mat[y][x] - 1
                        q.append([ny, nx])
                elif mat[y][x] > 0:
                    if mat[ny][nx] == 'D':
                        mat[ny][nx] = mat[y][x] + 1
                        return
                    if mat[ny][nx] == '.':
                        mat[ny][nx] = mat[y][x] + 1
                        q.append([ny, nx])
bfs()
print(mat[d_y][d_x] if mat[d_y][d_x] != 'D' else "KAKTUS")