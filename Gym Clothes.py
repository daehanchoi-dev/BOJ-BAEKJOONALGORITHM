def solution(n, lost, reserve):
    ans = 0
    for i in range(1, n+1):
        if i not in lost: # 안 잃어버린 학생
            ans +=1
        else:
            if i in reserve: # 잃어버렸지만 여분이 있는 학생
                ans +=1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: # 잃어버리고 여분도 없는 학생
        if i-1 in reserve:
            ans +=1
            reserve.remove(i-1)
        elif i+1 in reserve:
            ans +=1
            reserve.remove(i+1)

    return ans



