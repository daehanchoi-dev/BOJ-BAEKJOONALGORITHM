def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        skill_list = list(skill)

        for temp in s:
            if temp in skill:
                if temp != skill_list.pop(0): # (CBD를 순서대로 가져오기 위해 pop을 활용)
                    break
        else: # for-else 문을 활용 ( for 문이 끊기지 않고 끝까지 실행되면 else 문을 실행한다 )
            answer += 1
    return answer

