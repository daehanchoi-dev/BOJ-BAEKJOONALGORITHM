routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    routes = [[i[0], i[1]] for i in sorted(routes, key=lambda x: (x[0]))]
    # 배열 순서를 고속도로 진입 시점이 가장 빠른(-20) 지점부터 정렬
    result = [routes.pop(0)]  # 0 번째 배열 pop

    print('routes :', routes)
    print('result :', result)

    for i in routes:
        idx = 0
        while idx != len(result):
            if (result)[idx][0] <= i[0] <= result[idx][1] or (result[idx][0] <= i[1] <= result[idx][1]):
                result[idx][0] = i[0] if i[0] > result[idx][0] else result[idx][0]
                result[idx][1] = i[1] if i[1] < result[idx][1] else result[idx][1]
                # pop 해서 얻은 result 배열과 남은 routes 배열들을 비교해가면서 범위를 좁혀나간다.(ex:-20 에서 -18로)
                break
            else:
                idx += 1
            # 계속 비교해나가면서 좁혀지는 범위안에 들어오지 못하는 배열이 생기면
            # 그 만큼의 범위를 단속하기 위한 새 감시카메라를 설치한다.
        if idx == len(result):
            result.append(i)

    return len(result)

print(solution(routes))

