from collections import deque

n, m = map(int, input().split(' '))


def bfs(c):
    queue = deque()
    queue.append(start)
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                queue.append(y)
                visited[y] = True

    return visited[end]


adj = [[] for _ in range(n + 1)]
max_weight = 1
min_weight = 1000000000

for _ in range(m):
    x, y, weight = map(int, input().split(' '))
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    max_weight = max(max_weight, weight)
    min_weight = min(min_weight, weight)

start, end = map(int, input().split(' '))

while min_weight <= max_weight:
    mid = (min_weight + max_weight) // 2
    if bfs(mid):
        result = mid
        min_weight = mid + 1
    else:
        max_weight = mid - 1

print(result)