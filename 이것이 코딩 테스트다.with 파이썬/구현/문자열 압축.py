"""
프로그래머스 문제(2020 카카오 신입 공채) https://programmers.co.kr/learn/courses/30/lessons/60057
"""

def solution(s):
    answer = len(s)
    # 문자의 개수를 1개 단위부터 늘려가며 (전체 문자의 길이 / 2) 까지 확인
    for i in range(1, len(s) // 2 + 1 ):
        # 앞에서 부터 i(문자의 개수)만큼의 문자열 추출
        prev = s[0:i]
        # 압축된 문자를 저장할 compressed
        compressed = ""
        # 동일한 문자가 나와서 압축한 횟수
        count = 1
        # 단위(i) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(i, len(s), i):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j + i]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                # 한 번이라도 압축이 압축이 되었다면 압축 횟수 + 압축된 문자 출력, 아니면 문자 출력
                compressed += str(count) + prev if count >=2 else prev
                # 다시 상태 초기화
                prev = s[j:j + i]
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >=2 else prev
        # 위 과정을 통해 만들어지는 압축 문자열 중 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

s = "abcabcdede"
print(solution(s))