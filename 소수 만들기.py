from itertools import combinations

def check(a, b ,c):
    Sum = a + b + c
    for i in range(2, Sum):
        if Sum % 2 == 0:
            False
    return True

def main(num):
    ans = 0
    temp = list(combinations(num, 3))
    for i in temp:
        if check(temp[0], temp[1], temp[2]):
            ans += 1
    return ans


