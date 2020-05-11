# 1
answer =0
def dfs(idx, numbers, target, value):
    global answer
    n = len(numbers)
    if(idx == n and target == value):
        answer += 1
        return
    if(idx == n):
        return

    dfs(idx+1,numbers,target,value+numbers[idx])
    dfs(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0,numbers,target,0)
    return answer


# 2
def solution(numbers, target):
    if not numbers and target ==0:
        print("1st\n")
        return 1
    elif not numbers:
        print("2nd\n")
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

numbers = [1,1,1,1,1]
solution(numbers, 3)
print(solution(numbers, 3))