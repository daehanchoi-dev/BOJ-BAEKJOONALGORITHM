# BFS & DFS
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    c = 0
    q = deque()
    q.append(x)
    visit = [0] * (n+1)
    visit[x] = 1
    while q:
        here = q.popleft()
        c += 1
        for i in T[here]:
            if not visit[i]:
                visit[i] = 1
                q.append(i)
    return c


n, m = map(int, input().split())
T = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    T[b].append(a)

han = 0
result = []
for i in range(1, n+1):
    if T[i]:
        tmp = bfs(i)
        if han <= tmp:
            if han < tmp:
                result =[]
            han = tmp
            result.append(i)

print(*result)

