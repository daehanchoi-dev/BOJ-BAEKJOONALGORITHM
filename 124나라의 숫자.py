def solution(n):
    answer = ''

    # 1. 3으로 나눈 나머지에 매칭되는 숫자
    num_dict = {1: "1", 2: "2", 0: "4"}
    mok = 1 #몫
    na = 1  #나머지

    # 2. 몫이 0이 될 때까지 숫자를 만듦
    while mok != 0:
        mok = n // 3
        na = n % 3
        # 나머지가 0이라면 몫을 1 감소
        if na == 0:
            mok -= 1


        n = mok
        # 기존 answer에 앞부분에 하나씩 숫자를 붙여서 만듦
        answer = num_dict[na] + answer
    return answer