"""
1번 문제

a, b, c = map(int, input().split())

Long_Cycle = 0
for i in range(a, b + 1):
    cnt = 1
    while (True):
        if i % 2 == 0:
            i /= 2
            cnt += 1
        if i == 1:
            break
        if i % 2 == 1:
            if ((i * 3) + 1) > (b / 3) and c > 0:
                i = (i * 3) + 11
                c -= 1
                cnt += 1
            else:
                i = (i * 3) + 1
                cnt += 1
    if cnt > Long_Cycle:
        Long_Cycle = cnt
print(Long_Cycle)
"""


