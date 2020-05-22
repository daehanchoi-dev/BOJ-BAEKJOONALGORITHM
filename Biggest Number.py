
numbers = [6,10,2]
num = [3,30,34,5,9]

import functools

def comparator(a,b):
    if a + b > b + a:
        return 1
    else:
        return -1

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


print(solution(numbers))