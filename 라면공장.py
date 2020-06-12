def solution(stock, dates, supplies, k):
    import heapq

    answer = 0
    # 범위 시작점입니다.
    idx = 0
    # 1. 최대 힙 기반 우선순위 큐를 생성합니다.
    pq = []

    # 2. stock < k일 때까지 다음을 반복합니다.
    while stock < k:
        # 1. idx ~ dates의 끝까지 반복합니다.
        for i in range(idx, len(dates)):
            # 1. stock 이 dates[i]보다 작으면 반복을 멈춥니다.
            if stock < dates[i]:
                break
            # 2. 우선순위 큐에 supplies[i]를 넣습니다.
            heapq.heappush(pq, -supplies[i])
            # 3. 시작점을 i+1지점으로 옮깁니다.
            idx = i + 1

        # 2. 우선순위 큐에서 데이터를 꺼내 stock에 더해줍니다.
        stock += (heapq.heappop(pq) * -1)
        # 3. 공급 횟수 answer에 1을 더해줍니다.
        answer += 1

    return answer