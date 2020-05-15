answer = [1,2,3,4,5]
def solution(answer):
    ans = []
    scores = [0, 0, 0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]


    k = len(answer)

    for i in range(k):
        if answer[i] == first[i % len(first)]:
            scores[0] += 1

    for i in range(k):
        if answer[i] == second[i % len(second)]:
            scores[1] += 1

    for i in range(k):
        if answer[i] == third[i % len(third)]:
            scores[2] +=1
    # 각각의 배열(first, second, third) 마다 순환주기가 다르기 때문에 i % len(first)와 같이 각각 순환주기로 나눠줘야 한다.
    max_score = max(scores)

    for i in range(3):
        if scores[i] == max_score:
            ans.append(i+1)

    return ans

print(solution(answer))

