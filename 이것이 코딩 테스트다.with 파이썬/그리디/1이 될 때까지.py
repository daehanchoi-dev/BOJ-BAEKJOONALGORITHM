N, K = map(int, input().split()) # 공백을 구분하여 입력 받기
result = 0

while True:
    if N % K == 0:  # N 이 K 로 나누어 떨어진다면 나누기
        N /= K      # N 은 N 을 K 로 나눈 몫이 된다
        result += 1
    else:
        N -= 1      # N 이 K 로 나누어 떨이지지 않는다면 1 빼기
        result += 1
    if N == 1:      # N 이 1 이 된다면 그만..
        break

print(result)
