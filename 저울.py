def solution(weight):
    answer = 0
    weight = sorted(weight)
    weight2 = []
    weight2.append(weight[0])

    for i in range(1, len(weight)):  # 누적합 생성
        temp = weight[i] + weight2[i - 1]
        weight2.append(temp)

    if weight[0] != 1:
        return 1

    for num in range(1, len(weight) - 1):
        if weight2[num] + 1 < weight[num + 1]:
            answer = weight2[num] + 1
            return answer
            break
    if answer == 0:
        answer = weight2[len(weight2) - 1] + 1
        return answer