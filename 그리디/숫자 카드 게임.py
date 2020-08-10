N, M = map(int, input().split()) # 공백을 구분하여 입력받기

result = 0

for i in range(N):
    Card = list(map(int, input().split())) # 카드 행렬을 한 줄씩 입력받아서 한 줄씩 확인
    min_value = min(Card) # 현재 줄에서 가장 작은 수 찾기
    result = max(result, min_value) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)