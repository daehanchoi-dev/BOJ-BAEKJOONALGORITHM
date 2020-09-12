from itertools import combinations
from collections import Counter
import collections

def solution(orders, course):
    answer = []
    for c in course:
        array = []
        temp = []
        for o in range(len(orders)):
            candidate = list(combinations(orders[o], c))
            array += candidate


        count = collections.Counter(array)
        max_value = max(list(count.values()))
        for key in list(count.keys()):
            if count[key] == max_value:
                temp.append(key)
                temp.sort()
        answer += temp
        answer.sort()
    

    return answer

orders =["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course =[2,3,4]
print(solution(orders, course))
"""
for c in course:
    array = []
    temp = []
    for o in range(len(orders)):
        candidate = list(combinations(orders[o], c))
        array += candidate
    print('array=',array)

    count = collections.Counter(array)
    max_value = max(list(count.values()))
    for key in list(count.keys()):
        if count[key] == max_value:
            temp.append(key)
            temp.sort()
    answer.append(temp)
    answer.sort()
    print(temp)

print(answer)

"""


"""
counter = defaultdict(int)
for item in array:
    counter[item] += 1
print(counter)
counter = sorted(counter.items(), key=lambda kv: kv[1], reverse=True, )[:1]
print(counter)
array = []
"""
"""
count = Counter(array)
count = count.most_common(True)
print(count)
array = []
"""



