n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
sum = 0
end = 0

# i(시작점)를 차례대로 증가시키며 이동
for i in range(n):
    # end를 가능한 만큼 이동시키기
    while sum < m and end < n:
        sum += data[end]
        end += 1
    # 부분 합이 m일 때 카운트 증가
    if sum == m:
        cnt +=1
    sum -= data[i]
print(cnt)
