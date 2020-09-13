#2번
from collections import deque
ball =[11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]
result = []
idx = [0]
q = deque(ball)
while q:
    print(ball, order)
    print(q, idx)
    if order[0] == ball[0]:
        q.popleft()
        result.append(order[0])

        del order[0]
        del ball[0]
    elif order[0] == ball[-1]:
        q.reverse()
        q.popleft()
        q.reverse()
        result.append(order[0])

        del order[0]
        del ball[-1]

    else:
        idx.append(order[0])
        del order[0]
    print(q,'mr')
    if not ball:
        for i in range(len(q)):
            q.popleft()
            print(q)
    print(result)
    if idx:
        while True:
            if ball[0] in idx or ball[-1] in idx:
                print('welcome')
                for i in range(len(idx)):
                    if idx[i] == ball[0]:
                        print(idx[i], ball[0])
                        result.append(idx[i])
                        del ball[0]
                        del idx[i]
                    elif idx[i] == ball[-1]:
                        print('pop',idx[i], ball[-1])

                        result.append(idx[i])
                        del ball[-1]
                        del idx[i]
                        print('야야',ball, idx)
            else:
                print('없소')
                break

    print('result=',result)



"""
1번
def solution(boxes):
    idx2 = 0
    answer = len(boxes)
    for idx in range(len(boxes)):
        cnt = 0
        for i in range(len(boxes)):
            for j in range(2):
                if boxes[idx][idx2] == boxes[idx][idx2 + 1] or boxes[idx][idx2] == boxes[i][j]:
                    cnt += 1

        if cnt >= 2:
            answer -= 1
    return answer
"""