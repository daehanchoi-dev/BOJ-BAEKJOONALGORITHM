import heapq
import sys
input = sys.stdin.readline
# 무한을 의미하는 값으로 10억 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담고 있는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    # 모든 노드가 저장될 큐 생성
    q = []
    # 그래프의 시작 노드과 시작 노드의 거리(0)를 최소힙에 넣기
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어 있지 않다면
    while q:
        # 큐에서 노드를 하나씩 꺼내 인접한 노드들의 가중치를 모두 확인하고 거리가 가장 짧은 노드에 대한 정보 꺼내기
        current_distance, current_node = heapq.heaqpop(q)
        # 더 짧은 경로가 있다면 무시
        if distance[current_node] < current_distance:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adjacent, weight in graph[current_node].items():
            dist = current_distance + weight
            # 시작 노드에서 인접 노드로 바로 가는 것보다 현재 노드를 통해 가는 것이 더 가까울 경우
            if dist < distance[adjacent]:
                # 거리 업데이트
                distance[adjacent] = dist
                heapq.heappush(q, (dist, adjacent))
    return distance


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(Infinity)이라고 출력
    if distance[i] == INF:
        print("Infinity")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
