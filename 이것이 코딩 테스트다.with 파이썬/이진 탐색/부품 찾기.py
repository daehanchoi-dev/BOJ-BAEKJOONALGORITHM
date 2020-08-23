"""
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자

입력조건 :
- 첫째 줄에 정수 N이 주어진다.
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
- 셋째 줄에는 정수 M이 주어진다
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.이때 정수는 1보다 크고 10억 이하이다.

출력조건 :
- 첫째 줄에는 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력한다.
"""

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 큰 경우 오른쪽 확인
        else:
            start = mid +1
    return None

# 입력조건에 따른 입력
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
customer = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in customer:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no')
