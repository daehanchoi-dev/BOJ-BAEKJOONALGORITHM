from collections import deque

def bfs(x):
    q.append(x)
    c[x] = 1
    while q:
        x = q.popleft()
        for nx in a[x]:
            if c[nx] == 0:
                c[nx] = -1*c[x]
                q.append(nx)
            elif c[nx] == c[x]:
                return 1
    return 0

tc = int(input())
while tc:
    v, e = map(int, input().split())
    a = [[] for _ in range(v)]
    c = [0 for _ in range(v)]
    q = deque()
    for _ in range(e):
        x, y = map(int, input().split())
        a[x-1].append(y-1)
        a[y-1].append(x-1)
    ans = 0
    for i in range(v):
        if c[i] == 0:
            ans = bfs(i)
            if ans == 1:
                break
    if ans == 0:
        print("YES")
    else:
        print("NO")
    tc -= 1