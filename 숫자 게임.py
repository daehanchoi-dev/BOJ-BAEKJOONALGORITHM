A = [5,1,3,7]
B = [2,2,6,8]

"""
정확성 테스트 통과 // 효율성 테스트 통과 못함
def solution(A, B):
    answer = 0
    n = len(A)
    m = len(B)
    C = []
    for i in range(n):
        idx = 0
        result = max(B)
        print(result)
        for j in range(m):
            if A[i] < B[j]:
                result = min(result, B[j])
                print(result)
                idx = 1
        if idx == 1:

            C.append(result)
            B.remove(result)
            B.append(0)
            print(B)
            print('C',C)

    answer = len(C)
    return answer

print(solution(A,B))
"""
def solution(A,B):
    answer = 0
    A=sorted(A,reverse=True)
    B=sorted(B,reverse=True)
    for i in A:
        result = i
        for j in range(len(B)):
            if B[j]>v_min:
                result =B[j]
            else:
                break
        if result ==i:
            pass
        else:
            B.remove(result)
            answer += 1
    return answer