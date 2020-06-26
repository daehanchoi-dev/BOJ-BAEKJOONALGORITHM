import sys

def solution(morning, night, tree):
    # morning = 낮에 간 거리
    # night = 밤에 미끄러진 거리
    # tree = 나무 높이
    # cur_height = 현재 높이
    # day : 일

    if morning >= tree:
        return 1

    temp = (morning - night)
    day = (tree - morning) // temp

    if (tree - morning) % temp == 0:
        return day +1
    else:
        return day +2

if __name__ == "__main__":
    a, b, v = map(int, sys.stdin.readline().split())
    print(solution(a, b, v))