from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = [list(input()) for _ in range(n)]
cnt = 0
house = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global cnt
    m[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if m[nx][ny] == '1':
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if m[i][j] == '1':
            cnt = 0
            dfs(i, j)
            house.append(cnt)

print(len(house))
house.sort()
for i in house:
    print(i)