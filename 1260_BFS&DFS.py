from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in pro[v]:
        if not(visited[i]):
            dfs(i)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for i in pro[v]:
                if not visited[i]:
                    q.append(i)


N, M, v = map(int, input().split())
pro = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    pro[x].append(y)
    pro[y].append(x)

for i in pro:
    i.sort()

visited = [False] * (N+1)
dfs(v)
print()
visited = [False] * (N+1)
bfs(v)


