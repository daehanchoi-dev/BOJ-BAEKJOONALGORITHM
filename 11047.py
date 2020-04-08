# 동전 (Greedy)
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0

for i in range(1, N + 1):
    coin = coins[-i]
    print('coin = ', coin)
    while True:
        if K >= coin:
            K -= coin
            cnt += 1
            if K == 0:
                break
        else:
            break

print(cnt)
