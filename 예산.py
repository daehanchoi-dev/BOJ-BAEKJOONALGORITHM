def solution(budgets, M):
    mins, maxs= 0, max(budgets)
    ans = 0
    while mins <= maxs:
        mid = (mins+maxs) // 2
        temp = [i if i < mid else mid for i in budgets]
        if sum(temp) > M:
            maxs = mid -1
        elif sum(temp) <= M:
            ans = mid
            mins = mid + 1
    return ans

