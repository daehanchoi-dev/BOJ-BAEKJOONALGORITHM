N, M = map(int, input().split())

def input_str():
    return [list(map(int, list(input()))) for _ in range(N)]

a, b = input_str(), input_str()

def flip(x,y,a):
    for i in range(3):
        for j in range(3):
            a[x+i][y+j] ^= 1


ans = 0

for i in range(N-2):
    for j in range(0, M-2):
        if a[i][j] != b[i][j]:
            flip(i,j,a)
            ans +=1

print(ans if a==b else -1)