# 유기농 배추 ( BFS, DFS )
import sys
sys.setrecursionlimit(50000)

T = int(input())
cabbage, mark = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global cabbage, mark
    if mark[x][y] == 1:
        return
    mark    [x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y+dy[i]
        if cabbage[xx][yy] == 0 or mark[xx][yy]:
            continue
        dfs(xx, yy)


def main():
    global cabbage, mark
    M, N, K = map(int, input().split())
    cabbage = [[0 for i in range(50+2)] for _ in range(50+2)]
    mark = [[0 for i in range(50+2)] for _ in range(50+2)]
    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y+1][x+1] = 1

    ans =0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if cabbage[i][j] ==0 or mark[i][j] ==1:
                continue
            dfs(i,j)
            ans +=1
    print(ans)



for _ in range(T):
    main()





