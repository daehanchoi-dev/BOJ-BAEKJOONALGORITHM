

M, N = map(int, input().split())

Chess = [list(input()) for _ in range(M)]

x = len(Chess)-7
y = len(Chess[0])-7
Min_cnt = 64
cnt = 0

for i in range(x):
    for j in range(y):
        cnt = 0
        w_b = Chess[x][y]

        for a in range(8):
            for b in range(8):
                if ((a + b) % 2 == 0 and w_b != Chess[i+a][j+b]):
                    cnt += 1
                elif ((a+b) % 2 == 1 and w_b == Chess[i+a][j+b]):
                    cnt += 1
        if (Min_cnt > cnt and cnt !=0):
            Min_cnt = cnt

print(Min_cnt)
