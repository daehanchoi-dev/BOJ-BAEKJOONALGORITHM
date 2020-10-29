def solution(n):
    answer = 0
    while n > 0:
        a, b = divmod(n, 2)
        n = a
        if b != 0:
            answer += 1
    return answer

