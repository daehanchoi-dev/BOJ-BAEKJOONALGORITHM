def solution(tickets):
    def helper(tickets, route):
        if tickets == []:
            return route
        left = [i for i in range(len(tickets)) if tickets[i][0] == route[-1]]
        if left == []:
            return None
        left.sort(key = lambda i: tickets[i][1])

        for next in left:
            rest = helper(tickets[:next]+tickets[next+1:], route+[tickets[next][1]])
            if rest is not None:
                return rest
    return helper(tickets, ["ICN"])