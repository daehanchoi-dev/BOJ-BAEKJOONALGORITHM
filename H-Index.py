
def solution(citations):
    ans = 0
    array = []
    for i in range(len(citations)): # 배열 전체의 크기만큼 반복 ( 0부터 -1(끝지점) 까지 전부 비교하기 위해)
        temp = 0
        for j in range(len(citations)):
            if citations[j] >= citations[i]: # 처음 비교하는 [0]번째 배열보다 큰 인덱스 값 모두 조사
                temp += 1  # 큰 인덱스 값이 존재할 때 마다 temp +1
            if temp >= citations[i]: # 조사 후 [0]번째 배열보다 큰 인덱스 값이 [0] 인덱스 값 보다 클 경우 array 배열에 추가
                array.append(citations[i])
    array = list(set(array)) # array 배열의 중복 값 제거
    ans = max(array) # array 배열의 최대 값 반환
    return ans

citations = [3,0,6,1,5,4,7,8,9]
print(solution(citations))

"""
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


citations = [3,0,6,1,5]
print(solution(citations))
"""