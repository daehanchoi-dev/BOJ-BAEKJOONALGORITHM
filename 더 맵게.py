def solution(scoville, K):
    import heapq
    count = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        if n1 < K or n2 < K :
            heapq.heappush(scoville, n1+(n2*2))
            count += 1
        else :
            return count
    if scoville[0] > K:
        return count
    else :
        return -1