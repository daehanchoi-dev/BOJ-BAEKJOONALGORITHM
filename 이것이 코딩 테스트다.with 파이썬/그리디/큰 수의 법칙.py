n, m, k = map(int, input().split()) # 공백을 구분하여 입력받기
data = list(map(int, input().split())) # n개의 수를 구분하여 입력받기

data.sort(reverse=True) # 입력받은 수 정렬
result = 0 # 결과 값 초기화


while True:
    for i in range(k): # k 를 초과하지 않을 만큼
        if m == 0:
            break
        result += data[0] # 첫 번째로 큰 수 더하기
        m -= 1
    if m == 0:
        break
    result += data[1] # 두 번째로 큰 수 더하기
    m -= 1

print(result)

"""
n, m, k = map(int, input().split()) # 공백을 구분하여 입력받기
data = list(map(int, input().split())) # n개의 수를 구분하여 입력받기

data.sort(reverse=True) # 입력받은 수 정렬

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * data[0] # 가장 큰 수 더하기
result += (m - count) * data[1] # 두 번째로 큰 수 더하기

print(result)

"""
