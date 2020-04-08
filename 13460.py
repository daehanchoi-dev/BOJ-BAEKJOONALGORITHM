import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 2개의 구슬 좌표 x,y를 4차원으로 배열에 선언하고 False로 초기화 이 후 방문여부 체크 하고 방문 안했다면 queuq 에 넣고 True로 체크
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = (-1, 1, 0, 0)   # (왼쪽 오른쪽 위 아래) x 좌표 의미
dy = (0, 0, -1, 1)   # (왼쪽 오른쪽 위 아래) y 좌표 의미
q = deque()


def init():
    rx, ry, bx, by = [0] *4  # 빨간 파란 공의 위치 초기화
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i,j
            if board[i][j] == 'B':
                bx, by = i,j

    print('빨간 공의 위치 :', (rx, ry), '파란 공의 위치 :', (bx, by))
    q.append((rx, ry, bx, by, 1))  # 1은 depth
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    cnt = 0 # 이동한 칸 수
    while board[x+dx][y+dy] !='#' and board[x][y] !='0':
        x += dx
        y += dy
        cnt +=1

    return x,y, cnt


def bfs():
    init()
    while q:
        rx, ry, bx, by, depth =q.popleft()
        if depth > 10:  # 공이 10번 이상 이동하면 종료
            break
        for i in range(len(dx)):
            Nrx, Nry, rcnt = move(rx, ry, dx[i], dx[i]) # 빨간 공 움직임
            Nbx, Nby, bcnt = move(bx, by, dx[i], dx[i]) # 파란 공 움직임

            print('depth :', depth, "방향 :", dx[i],dy[i], '빨간 공 위치:', Nrx, Nry, "파란 공 :", Nbx, Nby )

            if board[Nrx][Nry] == '0': # 빨간 공이 구멍에 떨어지면
                print('depth =', depth)
                return
            if board[Nbx][Nby] == '0': # 파란 공이 구멍에 떨어지면
                continue
            if Nrx == Nbx and Nry == Nby:  # 빨간 공과 파란 공의 위치가 같다면
                if rcnt > bcnt:    # 이동 거리가 더 많은 쪽이 뒤로 한칸 간다.
                    Nrx -= dx[i]
                    Nry -= dy[i]
                else:
                    Nbx -= dx[i]
                    Nby -= dy[i]

            # 방문 여부 확인
            if not visited[Nrx][Nry][Nbx][Nby]:
                visited[Nrx][Nry][Nbx][Nby] = True
                q.append((Nrx, Nry, Nbx, Nby, depth+1))

    print(-1)  # 실패

bfs()