node = int(input())
tree_info = [[] for _ in range(node + 1)]

for _ in range(node - 1):
    parent, child, length = map(int, input().split())
    tree_info[parent].append((child, length))



def bfs(graph_list, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        visited.append(node)
        for child in graph_list[node]:
            queue.append(child[0])

    return visited


# 정렬에 쓸 리스트 생성
bfs_node = bfs(tree_info, 1)
max_node = [0 for _ in range(node + 1)]
diameter = [[0] for _ in range(node + 1)]
max_diameter = [0 for _ in range(node + 1)]

# 최하단의 노드부터 일방향 최댓값, 지름 최댓값 추출
while bfs_node:
    temp = bfs_node.pop()

    for child in tree_info[temp]:
        try:
            child_length = max_node[child[0]] + child[1]
        except:
            child_length = child[1]
        diameter[temp].append(child_length)
        max_node[temp] = max(diameter[temp])

    max_diameter[temp] += max(diameter[temp])
    diameter[temp].remove(max(diameter[temp]))
    try:
        max_diameter[temp] += max(diameter[temp])
    except:
        pass

# 추출한 지름 값들 중 최댓값 출력
print(max(max_diameter))
