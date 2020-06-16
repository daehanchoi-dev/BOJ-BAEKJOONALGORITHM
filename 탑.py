h = [6,9,5,7,4]
"""
def solution(h):
    ans = []
    ans.append(0)
    temp = h[0]
    for i in range(1,len(h)):
        if temp > h[i]:
            ans.append(i)
        else:
            ans.append(0)
        temp = h[i]

    return ans

print(solution(h))
"""

def solution(h):
    answer = [0] * len(h)
    for i in range(len(h)-1,0,-1):
        for j in range(i-1,-1,-1):
            if h[i] < h[j]:
                answer[i] = j+1
                break
    return answer
