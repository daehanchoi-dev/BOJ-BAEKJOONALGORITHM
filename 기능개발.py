def solution(progresses, speeds):
    ans = []
    while len(progresses):  # Progresses 의 길이만큼 진행
        No = False # 작업 미완료
        cnt = 0 # 작업 완료
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while len(progresses) !=0  and progresses[0] >= 100: # 작업 할 것이 있고 첫 작업이 완료라면 반복
            No = True
            cnt += 1
            del progresses[0] # 완료된 작업 삭제
            del speeds[0] # 완료된 작업 삭제

        if No == True:
            ans.append(cnt)

    return ans

if __name__ == "__main__":
    progresses = [93,30,55]
    speeds = [1,30,5]
    res = solution(progresses,speeds)
    print(res)